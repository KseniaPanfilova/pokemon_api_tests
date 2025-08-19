import pytest


ITEM_NAMES = [
    pytest.param('safari-ball', id='Safari-ball'),
    pytest.param('potion', id='Potion'),
    pytest.param('burn-heal', id='Burn-heal')
]

ITEM_IDS = [
    pytest.param(5, 'safari-ball', id='5'),
    pytest.param(17, 'potion', id='17'),
    pytest.param(19, 'burn-heal', id='19')
]

LIST_PARAMS = [
    pytest.param(1, 0, id='1_item'),
    pytest.param(5, 0, id='5_items'),
    pytest.param(10, 5, id='10_items_offset_5')
]
