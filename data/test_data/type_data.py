import pytest


TYPE_NAMES = [
    pytest.param('flying', id='Flying'),
    pytest.param('steel', id='Steel'),
    pytest.param('dark', id='Dark')
]

TYPE_IDS = [
    pytest.param(3, 'flying', id='3'),
    pytest.param(9, 'steel', id='9'),
    pytest.param(17, 'dark', id='17')
]

LIST_PARAMS = [
    pytest.param(1, 0, id='1_type'),
    pytest.param(5, 0, id='5_types'),
    pytest.param(10, 5, id='10_types_offset_5')
]