from typing import Union, Literal

from .model import Language

LanguageLike = Union[Language, Literal[0, 1, 2, 3, 4]]
LiteralTier = Literal[100, 500, 1000, 2000, 5000, 10000]
