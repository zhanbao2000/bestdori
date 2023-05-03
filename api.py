from .model import SongsAll, Song, BandsAll, EventTrack, EventsAll
from .typing import LanguageLike, LiteralTier
from .utils import parse_url_as

__all__ = ['get_songs_all', 'get_song', 'get_bands_all', 'get_event_track', 'get_events_all']


async def get_songs_all(**kwargs) -> SongsAll:
    """Get all songs from bestdori"""
    return await parse_url_as('https://bestdori.com/api/songs/all.7.json', SongsAll, **kwargs)


async def get_song(song_id: int, **kwargs) -> Song:
    """Get a song from bestdori"""
    return await parse_url_as(f'https://bestdori.com/api/songs/{song_id}.json', Song, **kwargs)


async def get_bands_all(**kwargs) -> BandsAll:
    """Get all bands (name only) from bestdori"""
    return await parse_url_as('https://bestdori.com/api/bands/all.1.json', BandsAll, **kwargs)


async def get_event_track(server: LanguageLike, event: int, tier: LiteralTier, **kwargs) -> EventTrack:
    """Get event track from bestdori"""
    return await parse_url_as(f'https://bestdori.com/api/tracker/data?server={server}&event={event}&tier={tier}', EventTrack, **kwargs)


async def get_events_all(**kwargs) -> EventsAll:
    """Get all events from bestdori"""
    return await parse_url_as('https://bestdori.com/api/events/all.6.json', EventsAll, **kwargs)
