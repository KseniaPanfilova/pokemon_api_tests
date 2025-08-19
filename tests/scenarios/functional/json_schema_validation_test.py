import pytest
import allure
from data.schemas.pokemon_schema import pokemon_schema
from data.schemas.ability_schema import ability_schema
from data.schemas.move_schema import move_schema
from data.test_data.pokemon_data import POKEMON_NAMES
from data.test_data.ability_data import ABILITY_NAMES
from data.test_data.move_data import MOVE_NAMES


@pytest.mark.functional
@pytest.mark.parametrize('pokemon_name', POKEMON_NAMES)
@allure.description('Проверка соответсвия ответа для покемона json-схеме.\n'
                    'Цель: Убедиться, что ответ содержит все необходимые поля и значения полей нужных типов данных.')
def test_pokemon_json_schema(api, check, pokemon_name):
    with allure.step(f'Запрос покемона {pokemon_name}'):
        response = api.get_pokemon_by_name(pokemon_name)
        with allure.step(f'Проверка соответствия ответа json-схеме'):
            check.json_schema(response, schema=pokemon_schema)


@pytest.mark.functional
@pytest.mark.parametrize('ability_name', ABILITY_NAMES)
@allure.description('Проверка соответсвия ответа для способности json-схеме.\n'
                    'Цель: Убедиться, что ответ содержит все необходимые поля и значения полей нужных типов данных.')
def test_ability_json_schema(api, check, ability_name):
    with allure.step(f'Запрос способности {ability_name}'):
        response = api.get_ability_by_name(ability_name)
        with allure.step(f'Проверка соответствия ответа json-схеме'):
            check.json_schema(response, schema=ability_schema)


@pytest.mark.functional
@pytest.mark.parametrize('move_name', MOVE_NAMES)
@allure.description('Проверка соответсвия ответа для движения json-схеме.\n'
                    'Цель: Убедиться, что ответ содержит все необходимые поля и значения полей нужных типов данных.')
def test_ability_json_schema(api, check, move_name):
    with allure.step(f'Запрос движения {move_name}'):
        response = api.get_move_by_name(move_name)
        with allure.step(f'Проверка соответствия ответа json-схеме'):
            check.json_schema(response, schema=move_schema)
