import pytest
from src.pokemon_service import PokemonAPI
from utils.checks import Checks


base_url = 'https://pokeapi.co/api/v2/'


@pytest.fixture
def api():
    return PokemonAPI(base_url)


@pytest.fixture
def check():
    return Checks()
