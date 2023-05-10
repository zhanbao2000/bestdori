from io import BytesIO
from typing import Literal

from .api import get_cards_all
from .model import Attribute, Language
from .utils import get_online, get_region_prefix

__all__ = [
    'get_item_effect_description', 'get_card_thumb',
    'get_card_box', 'get_attribute_icon', 'get_band_icon',
    'get_card_star', 'get_degree_file', 'get_profile_card_image'
]

# 道具效果（百分比），例如 ITEM_EFFECT_BAND[7] == 2.5 表示 7  级乐器提升 5% 综合力
ITEM_EFFECT_BAND = [2, 2, 2.5, 3, 3.5, 4, 4.5, 5]
ITEM_EFFECT_EVERYONE = [1, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5]
ITEM_EFFECT_MAGAZINE = [8, 8, 10, 12, 14, 16, 18, 20]
ITEM_EFFECT_PLAZA = [2, 2, 4, 6, 8, 10, 12, 14]
ITEM_EFFECT_MENU = [2, 2, 4, 6, 8, 10, 12, 14]

# 映射道具 ID 到作用域与效果分类
ITEM_SCOPE = {
    # 乐队
    **dict.fromkeys((1, 6, 11, 16, 21, 26, 31), ('Poppin\'Party 全员综合力', ITEM_EFFECT_BAND)),
    **dict.fromkeys((2, 7, 12, 17, 22, 27, 32), ('Afterglow 全员综合力', ITEM_EFFECT_BAND)),
    **dict.fromkeys((3, 8, 13, 18, 23, 28, 33), ('Pastel＊Palettes 全员综合力', ITEM_EFFECT_BAND)),
    **dict.fromkeys((4, 9, 14, 19, 24, 29, 34), ('Roselia 全员综合力', ITEM_EFFECT_BAND)),
    **dict.fromkeys((5, 10, 15, 20, 25, 30, 35), ('Hello，Happy World！ 全员综合力', ITEM_EFFECT_BAND)),
    **dict.fromkeys((83, 84, 85, 86, 87, 88, 89), ('Morfonica 全员综合力', ITEM_EFFECT_BAND)),
    **dict.fromkeys((90, 91, 92, 93, 94, 95, 96), ('RAISE A SUILEN 全员综合力', ITEM_EFFECT_BAND)),
    **dict.fromkeys((73, 74, 75, 76, 77, 78, 79), ('所有成员的综合力', ITEM_EFFECT_EVERYONE)),
    # 四色
    66: ('所有 Cool 属性成员的综合力', ITEM_EFFECT_PLAZA),
    67: ('所有 Happy 属性成员的综合力', ITEM_EFFECT_PLAZA),
    69: ('所有 Pure 属性成员的综合力', ITEM_EFFECT_PLAZA),
    70: ('所有 Powerful 属性成员的综合力', ITEM_EFFECT_PLAZA),
    57: ('所有 Cool 属性成员的综合力', ITEM_EFFECT_MENU),
    58: ('所有 Happy 属性成员的综合力', ITEM_EFFECT_MENU),
    60: ('所有 Pure 属性成员的综合力', ITEM_EFFECT_MENU),
    56: ('所有 Powerful 属性成员的综合力', ITEM_EFFECT_MENU),
    # 分综合力
    80: ('所有成员的 Performance 数值', ITEM_EFFECT_MAGAZINE),
    81: ('所有成员的 Technique 数值', ITEM_EFFECT_MAGAZINE),
    82: ('所有成员的 Visual 数值', ITEM_EFFECT_MAGAZINE),
}


def get_item_effect_description(item_id: int, item_level: int) -> str:
    scope, effect_list = ITEM_SCOPE[item_id]
    effect = effect_list[item_level]
    return f'{scope}上升 {effect}%'


async def get_card_thumb(card_id: int, is_after_training: bool, region: Language) -> BytesIO:
    """Get card thumb by card id."""
    cards_all = await get_cards_all(is_cache=True)
    if card_id not in cards_all.__root__:
        cards_all = await get_cards_all(is_cache=False)

    card = cards_all.__root__[card_id]
    card_res_set = card.resourceSetName
    card_rip_id = str(int(card_id / 50)).zfill(5)
    card_suffix = 'after_training' if is_after_training else 'normal'
    url = f'https://bestdori.com/assets/{get_region_prefix(region)}/thumb/chara/card{card_rip_id}_rip/{card_res_set}_{card_suffix}.png'

    return BytesIO(await get_online(url))


async def get_card_box(rarity: int, attribute: Attribute) -> BytesIO:
    """Get card box by rarity and attribute."""
    if rarity == 1:
        return BytesIO(await get_online(f'https://bestdori.com/res/image/card-1-{attribute.value}.png'))
    return BytesIO(await get_online(f'https://bestdori.com/res/image/card-{rarity}.png'))


async def get_attribute_icon(attribute: Attribute) -> BytesIO:
    """Get attribute icon."""
    return BytesIO(await get_online(f'https://bestdori.com/res/icon/{attribute.value}.svg'))


async def get_band_icon(band_id: Literal[1, 2, 3, 4, 5, 18, 21]) -> BytesIO:
    """Get band icon."""
    return BytesIO(await get_online(f'https://bestdori.com/res/icon/band_{band_id}.svg'))


async def get_card_star(is_after_training: bool) -> BytesIO:
    """Get card star."""
    if not is_after_training:
        return BytesIO(await get_online('https://bestdori.com/res/icon/star.png'))
    return BytesIO(await get_online('https://bestdori.com/res/icon/star_trained.png'))


async def get_degree_file(filename: str, region: Language) -> BytesIO:
    """Get degree icon or background, filename without .png suffix."""
    return BytesIO(await get_online(f'https://bestdori.com/assets/{get_region_prefix(region)}/thumb/degree_rip/{filename}.png'))


async def get_profile_card_image(card_id: int, is_after_training: bool, region: Language) -> BytesIO:
    """Get card profile sized by card id."""
    cards_all = await get_cards_all(is_cache=True)
    if card_id not in cards_all.__root__:
        cards_all = await get_cards_all(is_cache=False)

    card = cards_all.__root__[card_id]
    card_res_set = card.resourceSetName
    card_suffix = 'after_training' if is_after_training else 'normal'
    url = f'https://bestdori.com/assets/{get_region_prefix(region)}/characters/resourceset/{card_res_set}_rip/trim_{card_suffix}.png'

    return BytesIO(await get_online(url))
