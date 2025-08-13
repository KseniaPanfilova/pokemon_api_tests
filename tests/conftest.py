import pytest
from src.pokemon_service import PokemonAPI
from utils.checks import Checks
from tests.test_pokemons import TestPokemons
from tests.test_abilities import TestAbilities
from tests.test_moves import TestMoves
from tests.test_types import TestTypes
from tests.test_items import TestItems

base_url = 'https://pokeapi.co/api/v2/'


@pytest.fixture
def pokemon_api():
    return PokemonAPI(base_url)


@pytest.fixture
def check():
    return Checks()


@pytest.fixture
def pokemon_tester(pokemon_api, check):
    return TestPokemons(pokemon_api, check)


@pytest.fixture
def ability_tester(pokemon_api, check):
    return TestAbilities(pokemon_api, check)


@pytest.fixture
def move_tester(pokemon_api, check):
    return TestMoves(pokemon_api, check)


@pytest.fixture
def type_tester(pokemon_api, check):
    return TestTypes(pokemon_api, check)


@pytest.fixture
def item_tester(pokemon_api, check):
    return TestItems(pokemon_api, check)
