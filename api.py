from .model import SongsAll, Song, BandsAll, EventTrack, EventsAll, CardsAll, DegreesAll
from .typing import LanguageLike, LiteralTier
from .utils import parse_url_as

__all__ = ['get_songs_all', 'get_song', 'get_bands_all', 'get_event_track', 'get_events_all', 'get_cards_all', 'get_degrees_all']


async def get_songs_all(is_cache: bool = False) -> SongsAll:
    """Get all songs from bestdori"""
    return await parse_url_as('https://bestdori.com/api/songs/all.7.json', SongsAll, is_cache)


async def get_song(song_id: int, is_cache: bool = False) -> Song:
    """Get a song from bestdori"""
    return await parse_url_as(f'https://bestdori.com/api/songs/{song_id}.json', Song, is_cache)


async def get_bands_all(is_cache: bool = False) -> BandsAll:
    """Get all bands (name only) from bestdori"""
    return await parse_url_as('https://bestdori.com/api/bands/all.1.json', BandsAll, is_cache)


async def get_event_track(server: LanguageLike, event: int, tier: LiteralTier, is_cache: bool = False) -> EventTrack:
    """Get event track from bestdori"""
    return await parse_url_as(f'https://bestdori.com/api/tracker/data?server={server}&event={event}&tier={tier}', EventTrack, is_cache)


async def get_events_all(is_cache: bool = False) -> EventsAll:
    """Get all events from bestdori"""
    return await parse_url_as('https://bestdori.com/api/events/all.6.json', EventsAll, is_cache)


async def get_cards_all(is_cache: bool = False) -> CardsAll:
    """Get all cards from bestdori"""
    return await parse_url_as('https://bestdori.com/api/cards/all.5.json', CardsAll, is_cache)


async def get_degrees_all(is_cache: bool = False) -> DegreesAll:
    """Get all degrees from bestdori"""
    return await parse_url_as('https://bestdori.com/api/degrees/all.3.json', DegreesAll, is_cache)
