import pytest
import allure

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


@pytest.mark.smoke
@pytest.mark.parametrize('pokemon_name', POKEMON_NAMES)
@allure.description('Проверка получения покемона по названию.\n'
                    'Цель: убедиться, что можно получить данные о покемоне по его названию.')
def test_get_pokemon_by_name(api, checker, pokemon_name):
    with allure.step(f'Запрос покемона "{pokemon_name}"'):
        response = api.get_pokemon_by_name(pokemon_name)
        with allure.step('Проверка статус-кода ответа'):
            checker.status_code(response, 200)
        with allure.step(f'Проверка, что в ответе приходит покемон "{pokemon_name}"'):
            checker.json_value(response, field_name='name', expected_value=pokemon_name)


@pytest.mark.smoke
@pytest.mark.parametrize('pokemon_id, pokemon_name', POKEMON_IDS)
@allure.description('Тест получения покемона по ID.\n'
                    'Цель: убедиться, что можно получить данные о покемоне по его ID.')
def test_get_pokemon_by_id(api, checker, pokemon_id, pokemon_name):
    with allure.step(f'Запрос покемона c ID "{pokemon_id}"'):
        response = api.get_pokemon_by_id(pokemon_id)
        with allure.step('Проверка статус-кода ответа'):
            checker.status_code(response, 200)
        with allure.step(f'Проверка, что в ответе приходит покемон "{pokemon_name}"'):
            checker.json_value(response, field_name='name', expected_value=pokemon_name)


@pytest.mark.smoke
@pytest.mark.parametrize('limit, offset', LIST_PARAMS)
@allure.description('Тест получения списка покемонов.\n'
                    'Проверить, что список покемонов можно ограничить.')
def test_get_pokemons_list(api, checker, limit, offset):
    with allure.step(f'Запрос списка (limit={limit}, offset={offset})'):
        response = api.get_pokemons_list(limit, offset)
        with allure.step('Проверка статус-кода ответа'):
            checker.status_code(response, 200)
        with allure.step(f'Проверка, что в списке {limit} элементов'):
            checker.elements_count(response, limit)
        if offset > 0:
            with allure.step('Проверка правильности применения офсета'):
                checker.offset(response, offset, limit)


@pytest.mark.smoke
@allure.description('Тест обработки 404 ошибки.\n'
                    'Цель: убедиться, что API корректно обрабатывает ошибки.')
def test_404_for_invalid_pokemon(api, checker):
    with allure.step("Запрос несуществующего покемона"):
        response = api.get_pokemon_by_name('non_existent_pokemon')
        with allure.step('Проверка статус-кода ответа'):
            checker.status_code(response, 404)

