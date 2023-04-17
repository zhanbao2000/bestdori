from typing import TypeVar

from httpx import AsyncClient
from pydantic import BaseModel, parse_obj_as

T = TypeVar('T', bound=BaseModel)


async def parse_url_as(url: str, model: type[T], **kwargs) -> T:
    async with AsyncClient(**kwargs) as client:
        response = await client.get(url)
        response.raise_for_status()
    return parse_obj_as(model, response.json())
