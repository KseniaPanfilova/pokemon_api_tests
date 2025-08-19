import pytest


ABILITY_NAMES = [
    pytest.param('battle-armor', id='Battle-armor'),
    pytest.param('insomnia', id='Insomnia'),
    pytest.param('flash-fire', id='Flash-fire')
]

ABILITY_IDS = [
    pytest.param(4, 'battle-armor', id='4'),
    pytest.param(15, 'insomnia', id='15'),
    pytest.param(18, 'flash-fire', id='18')
]

LIST_PARAMS = [
    pytest.param(1, 0, id='1_ability'),
    pytest.param(5, 0, id='5_abilities'),
    pytest.param(10, 5, id='10_abilities_offset_5')
]