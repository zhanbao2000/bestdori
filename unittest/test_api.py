import pytest

from ..api import get_songs_all, get_song, get_bands_all, get_event_track, get_events_all
from ..model import Language


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


@pytest.mark.asyncio
async def test_get_bands_all():
    assert await get_bands_all()


@pytest.mark.asyncio
async def test_get_event_track():
    assert await get_event_track(Language.Japanese, 999, 100)  # empty cutoffs
    assert await get_event_track(Language.Japanese, 100, 100)


@pytest.mark.asyncio
async def test_get_events_all():
    assert await get_events_all()
