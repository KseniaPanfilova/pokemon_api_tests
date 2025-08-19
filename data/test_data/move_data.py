import pytest


MOVE_NAMES = [
    pytest.param('bind', id='Bind'),
    pytest.param('swords-dance', id='Swords-dance'),
    pytest.param('pay-day', id='Pay-day')
]

MOVE_IDS = [
    pytest.param(20, 'bind', id='20'),
    pytest.param(14, 'swords-dance', id='14'),
    pytest.param(6, 'pay-day', id='6')
]

LIST_PARAMS = [
    pytest.param(1, 0, id='1_move'),
    pytest.param(5, 0, id='5_moves'),
    pytest.param(10, 5, id='10_moves_offset_5')
]