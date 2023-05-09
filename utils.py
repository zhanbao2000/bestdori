import hashlib
from json import loads
from pathlib import Path
from typing import TypeVar, Optional

from httpx import AsyncClient, AsyncHTTPTransport
from pydantic import BaseModel, parse_obj_as

T = TypeVar('T', bound=BaseModel)


class CacheManager:

    def __init__(self, filename: str):
        self.filename = filename

        self.root = Path(__file__).parent / 'cache'
        if not self.root.exists():
            self.root.mkdir()

    def get(self) -> Optional[bytes]:
        if not (fullpath := self.root / self.filename).exists():
            return None
        with open(fullpath, 'rb') as f:
            return f.read()

    def save(self, content: bytes) -> None:
        with open(self.root / self.filename, 'wb') as f:
            f.write(content)


async def parse_url_as(url: str, model: type[T], is_cache: bool = False) -> T:
    return parse_obj_as(model, loads(await get_online(url, is_cache)))


async def get_online(url: str, is_cache: bool = True) -> bytes:
    url_hash = md5(url)

    if is_cache:
        if cm := CacheManager(url_hash).get():
            return cm

    async with client:
        resp = await client.get(url)
        resp.raise_for_status()
        content = resp.content
        CacheManager(url_hash).save(content)
        return resp.content


def md5(s: str) -> str:
    return hashlib.md5(s.encode('utf-8')).hexdigest().replace('-', '').lower()


client = AsyncClient(
    proxies='http://127.0.0.1:8889',
    timeout=15,
    transport=AsyncHTTPTransport(retries=3)
)
