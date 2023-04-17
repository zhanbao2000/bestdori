from .model import SongsAll, Song, BandsAll, EventTrack, EventsAll
from .typing import LanguageLike, LiteralTier
from .utils import parse_url_as


async def get_songs_all() -> SongsAll:
    """Get all songs from bestdori"""
    return await parse_url_as('https://bestdori.com/api/songs/all.7.json', SongsAll)


async def get_song(song_id: int) -> Song:
    """Get a song from bestdori"""
    return await parse_url_as(f'https://bestdori.com/api/songs/{song_id}.json', Song)


async def get_bands_all() -> BandsAll:
    """Get all bands (name only) from bestdori"""
    return await parse_url_as('https://bestdori.com/api/bands/all.1.json', BandsAll)


async def get_event_track(server: LanguageLike, event: int, tier: LiteralTier) -> EventTrack:
    """Get event track from bestdori"""
    return await parse_url_as(f'https://bestdori.com/api/tracker/data?server={server}&event={event}&tier={tier}', EventTrack)


async def get_events_all() -> EventsAll:
    """Get all events from bestdori"""
    return await parse_url_as('https://bestdori.com/api/events/all.6.json', EventsAll)
