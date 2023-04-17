import datetime
from enum import Enum, IntEnum
from typing import Optional

from pydantic import BaseModel


class Tag(str, Enum):
    Normal = 'normal'
    Anime = 'anime'
    TieUp = 'tie_up'


class DifficultyInt(IntEnum):
    Easy = 0
    Normal = 1
    Hard = 2
    Expert = 3
    Special = 4


class Language(IntEnum):
    Japanese = 0
    English = 1
    ChineseTraditional = 2
    ChineseSimplified = 3
    Korean = 4


class BPM(BaseModel):
    bpm: float
    start: float
    end: float


class SongsAll(BaseModel):
    """https://bestdori.com/api/songs/all.7.json"""

    class Song(BaseModel):
        class Tag(str, Enum):
            Normal = 'normal'
            Anime = 'anime'
            TieUp = 'tie_up'

        class Difficulty(BaseModel):
            playLevel: int
            publishedAt: Optional[list[Optional[datetime.datetime]]]

        tag: Tag
        bandId: int
        jacketImage: list[str]
        musicTitle: list[Optional[str]]
        publishedAt: list[Optional[datetime.datetime]]
        closedAt: list[Optional[datetime.datetime]]
        difficulty: dict[DifficultyInt, Difficulty]
        length: float
        notes: dict[DifficultyInt, int]
        bpm: dict[DifficultyInt, list[BPM]]

    __root__: dict[int, Song]


class Song(BaseModel):
    """https://bestdori.com/api/songs/359.json"""

    class Achievement(BaseModel):
        musicId: int  # 359
        achievementType: str  # "score_rank_b"
        rewardType: str  # "practice_ticket"
        rewardId: Optional[int]  # 2
        quantity: int  # 1

    class Difficulty(BaseModel):
        class MultiLiveScoreMap(BaseModel):
            musicId: int  # 359
            musicDifficulty: str  # "easy"
            multiLiveDifficultyId: int  # 2001
            multiLiveDifficultyType: str  # "daredemo"
            scoreS: int  # 3321000
            scoreA: int  # 2214000
            scoreB: int  # 1107000
            scoreC: int  # 184500
            scoreSS: int  # 4428000
            scoreSSS: Optional[int]  # 0

        playLevel: int  # 11
        multiLiveScoreMap: dict[int, MultiLiveScoreMap]
        notesQuantity: int  # 1000
        scoreC: int  # 36900
        scoreB: int  # 221400
        scoreA: int  # 442800
        scoreS: int  # 664200
        scoreSS: int  # 885600

    bgmId: str  # "bgm359"
    bgmFile: str  # "359_hell_or_hell"
    tag: Tag  # "normal"
    bandId: int  # 18
    achievements: list[Achievement]
    jacketImage: list[str]  # ["359_hell_or_hell"]
    seq: int  # 712
    musicTitle: list[Optional[str]]  # ["HELL! or HELL?", ...]
    lyricist: list[Optional[str]]  # ["織田あすか（Elements Garden）", ...]
    composer: list[Optional[str]]  # ["菊田大介（Elements Garden）", ...]
    arranger: list[Optional[str]]  # ["菊田大介（Elements Garden）", ...]
    howToGet: list[Optional[str]]  # ["楽曲プレゼントを受け取る", ...]
    publishedAt: list[Optional[datetime.datetime]]  # ["1632031200000", ...]
    closedAt: list[Optional[datetime.datetime]]  # ["4121982000000", ...]
    difficulty: dict[DifficultyInt, Difficulty]
    length: float  # 108.504
    notes: dict[DifficultyInt, int]  # {"0": 196, "1": 338, "2": 598, "3": 999, "4": 1196}
    bpm: dict[DifficultyInt, list[BPM]]


class BandsAll(BaseModel):
    """https://bestdori.com/api/bands/all.1.json"""

    class BandName(BaseModel):
        bandName: list[Optional[str]]

    __root__: dict[Language, BandName]
