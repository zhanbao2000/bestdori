import hashlib
from json import loads
from pathlib import Path
from typing import TypeVar, Optional

from httpx import AsyncClient, AsyncHTTPTransport
from pydantic import BaseModel, parse_obj_as

from .model import Language

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

    async with get_client() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        content = resp.content
        CacheManager(url_hash).save(content)
        return resp.content


def md5(s: str) -> str:
    return hashlib.md5(s.encode('utf-8')).hexdigest().replace('-', '').lower()


def get_band_id(character_id: int) -> int:
    return (character_id - 1) // 5 + 1


def get_client(proxies: Optional[str] = None, timeout: float = 15, retries: int = 0, **kwargs) -> AsyncClient:
    return AsyncClient(
        proxies=proxies,
        timeout=timeout,
        transport=AsyncHTTPTransport(retries=retries) if retries else None,
        **kwargs
    )


def get_region_prefix(region: Language) -> Optional[str]:
    if region == Language.Japanese:
        return 'jp'
    elif region == Language.ChineseSimplified:
        return 'cn'
