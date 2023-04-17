import pytest

from ..api import get_songs_all, get_song


@pytest.mark.asyncio
async def test_get_song_all():
    assert await get_songs_all()


@pytest.mark.asyncio
async def test_get_song():
    assert await get_song(1)
    assert await get_song(243)  # [FULL] FIRE BIRD
    assert await get_song(486)  # [超高難易度 新SPECIAL] HELL! or HELL?
    assert await get_song(1000)  # Legendary (English Version)
    assert await get_song(10001)  # 彩虹节拍
