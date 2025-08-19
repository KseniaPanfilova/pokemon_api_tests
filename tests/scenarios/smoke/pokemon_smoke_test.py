import pytest
import allure
from data.test_data.pokemon_data import POKEMON_NAMES, POKEMON_IDS, LIST_PARAMS


@pytest.mark.smoke
@pytest.mark.parametrize('pokemon_name', POKEMON_NAMES)
@allure.description('Проверка получения покемона по названию.\n'
                    'Цель: убедиться, что можно получить данные о покемоне по его названию.')
def test_get_pokemon_by_name(api, check, pokemon_name):
    with allure.step(f'Запрос покемона "{pokemon_name}"'):
        response = api.get_pokemon_by_name(pokemon_name)
        with allure.step('Проверка статус-кода ответа'):
            check.status_code(response, 200)
        with allure.step(f'Проверка, что в ответе приходит покемон "{pokemon_name}"'):
            check.json_value(response, field_name='name', expected_value=pokemon_name)


@pytest.mark.smoke
@pytest.mark.parametrize('pokemon_id, pokemon_name', POKEMON_IDS)
@allure.description('Тест получения покемона по ID.\n'
                    'Цель: убедиться, что можно получить данные о покемоне по его ID.')
def test_get_pokemon_by_id(api, check, pokemon_id, pokemon_name):
    with allure.step(f'Запрос покемона c ID "{pokemon_id}"'):
        response = api.get_pokemon_by_id(pokemon_id)
        with allure.step('Проверка статус-кода ответа'):
            check.status_code(response, 200)
        with allure.step(f'Проверка, что в ответе приходит покемон "{pokemon_name}"'):
            check.json_value(response, field_name='name', expected_value=pokemon_name)


@pytest.mark.smoke
@pytest.mark.parametrize('limit, offset', LIST_PARAMS)
@allure.description('Тест получения списка покемонов.\n'
                    'Проверить, что список покемонов можно ограничить.')
def test_get_pokemons_list(api, check, limit, offset):
    with allure.step(f'Запрос списка (limit={limit}, offset={offset})'):
        response = api.get_pokemons_list(limit, offset)
        with allure.step('Проверка статус-кода ответа'):
            check.status_code(response, 200)
        with allure.step(f'Проверка, что в списке {limit} элементов'):
            check.elements_count(response, limit)
        if offset > 0:
            with allure.step('Проверка правильности применения офсета'):
                check.offset(response, offset, limit)


@pytest.mark.smoke
@allure.description('Тест обработки 404 ошибки.\n'
                    'Цель: убедиться, что API корректно обрабатывает ошибки.')
def test_404_for_invalid_pokemon(api, check):
    with allure.step("Запрос несуществующего покемона"):
        response = api.get_pokemon_by_name('non_existent_pokemon')
        with allure.step('Проверка статус-кода ответа'):
            check.status_code(response, 404)

