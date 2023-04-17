from .model import SongsAll, Song, BandsAll
from .utils import parse_url_as


async def get_songs_all() -> SongsAll:
    """Get all songs from bestdori"""
    return await parse_url_as('https://bestdori.com/api/songs/all.7.json', SongsAll)


async def get_song(song_id: int) -> Song:
    """Get a song from bestdori"""
    return await parse_url_as(f'https://bestdori.com/api/songs/{song_id}.json', Song)


async def get_bands_all() -> BandsAll:
    """Get all bands from bestdori"""
    return await parse_url_as('https://bestdori.com/api/bands/all.json', BandsAll)
