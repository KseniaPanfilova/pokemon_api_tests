import pytest


POKEMON_NAMES = [
    pytest.param('pikachu', id='Pikachu'),
    pytest.param('charizard', id='Charizard'),
    pytest.param('bulbasaur', id='Bulbasaur')
]

POKEMON_IDS = [
    pytest.param(25, 'pikachu', id='25'),
    pytest.param(6, 'charizard', id='6'),
    pytest.param(1, 'bulbasaur', id='1')
]

LIST_PARAMS = [
    pytest.param(1, 0, id='1_pokemon'),
    pytest.param(5, 0, id='5_pokemons'),
    pytest.param(10, 5, id='10_pokemons_offset_5')
]