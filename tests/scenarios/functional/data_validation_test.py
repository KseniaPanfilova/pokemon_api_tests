import pytest
import allure
from schemas.pokemon_schema import pokemon_schema

POKEMON_NAMES = [
    pytest.param('pikachu', id='Pikachu'),
    pytest.param('charizard', id='Charizard'),
    pytest.param('bulbasaur', id='Bulbasaur')
]

ABILITY_FIELDS = []
MOVE_FIELDS = []
ITEM_FIELDS = []
TYPE_FIELDS = []


@pytest.mark.functional
@pytest.mark.parametrize('pokemon_name', POKEMON_NAMES)
@allure.description('Проверка соответсвия ответа для покемона json-схеме.\n'
                    'Цель: Убедиться, что ответ содержит все необходимые поля и значения полей нужных типов данных.')
def test_pokemon_json_data(api, check, pokemon_name):
    with allure.step(f'Запрос покемона {pokemon_name}'):
        response = api.get_pokemon_by_name(pokemon_name)
        with allure.step(f'Проверка соответствия ответа json-схеме'):
            check.json_schema(response, schema=pokemon_schema)
