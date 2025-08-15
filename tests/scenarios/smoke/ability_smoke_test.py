import pytest
import allure

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


@pytest.mark.smoke
@pytest.mark.parametrize('ability_name', ABILITY_NAMES)
@allure.description('Проверка получения способности по названию.\n'
                    'Цель: убедиться, что можно получить данные о способности по ее названию.')
def test_get_ability_by_name(api, checker, ability_name):
    with allure.step(f'Запрос способности "{ability_name}"'):
        response = api.get_ability_by_name(ability_name)
        with allure.step('Проверка статус-кода ответа'):
            checker.status_code(response, 200)
        with allure.step(f'Проверка, что в ответе приходит способность "{ability_name}"'):
            checker.json_value(response, field_name='name', expected_value=ability_name)


@pytest.mark.smoke
@pytest.mark.parametrize('ability_id, ability_name', ABILITY_IDS)
@allure.description('Тест получения способности по ID.\n'
                    'Цель: убедиться, что можно получить данные о способности по ее ID.')
def test_get_ability_by_id(api, checker, ability_id, ability_name):
    with allure.step(f'Запрос способности c ID "{ability_id}"'):
        response = api.get_ability_by_id(ability_id)
        with allure.step('Проверка статус-кода ответа'):
            checker.status_code(response, 200)
        with allure.step(f'Проверка, что в ответе приходит способность "{ability_name}"'):
            checker.json_value(response, field_name='name', expected_value=ability_name)


@pytest.mark.smoke
@pytest.mark.parametrize('limit, offset', LIST_PARAMS)
@allure.description('Тест получения списка способностей.\n'
                    'Проверить, что список способностей можно ограничить.')
def test_get_abilities_list(api, checker, limit, offset):
    with allure.step(f'Запрос списка (limit={limit}, offset={offset})'):
        response = api.get_abilities_list(limit, offset)
        with allure.step('Проверка статус-кода ответа'):
            checker.status_code(response, 200)
        with allure.step(f'Проверка, что в списке {limit} элементов'):
            checker.elements_count(response, limit)
        if offset > 0:
            with allure.step(f'Проверка, что применен офсет {offset}'):
                checker.offset(response, offset, limit)


@pytest.mark.smoke
@allure.description('Тест обработки 404 ошибки.\n'
                    'Цель: убедиться, что API корректно обрабатывает ошибки.')
def test_404_for_invalid_ability(api, checker):
    with allure.step("Запрос несуществующего покемона"):
        response = api.get_ability_by_name('non_existent_ability')
        with allure.step('Проверка статус-кода ответа'):
            checker.status_code(response, 404)
