import pytest
import allure

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


@pytest.mark.smoke
@pytest.mark.parametrize('type_name', TYPE_NAMES)
@allure.description('Проверка получения типа по названию.\n'
                    'Цель: убедиться, что можно получить тип по названию.')
def test_get_type_by_name(api, check, type_name):
    with allure.step(f'Запрос типа "{type_name}"'):
        response = api.get_type_by_name(type_name)
        with allure.step('Проверка статус-кода ответа'):
            check.status_code(response, 200)
        with allure.step(f'Проверка, что в ответе приходит тип "{type_name}"'):
            check.json_value(response, field_name='name', expected_value=type_name)


@pytest.mark.smoke
@pytest.mark.parametrize('type_id, type_name', TYPE_IDS)
@allure.description('Тест получения типа по ID.\n'
                    'Цель: убедиться, что можно получить данные о типе по его ID.')
def test_get_type_by_id(api, check, type_id, type_name):
    with allure.step(f'Запрос тип c ID "{type_id}"'):
        response = api.get_type_by_id(type_id)
        with allure.step('Проверка статус-кода ответа'):
            check.status_code(response, 200)
        with allure.step(f'Проверка, что в ответе приходит тип "{type_name}"'):
            check.json_value(response, field_name='name', expected_value=type_name)


@pytest.mark.smoke
@pytest.mark.parametrize('limit, offset', LIST_PARAMS)
@allure.description('Тест получения списка типов.\n'
                    'Проверить, что список типов можно ограничить.')
def test_get_types_list(api, check, limit, offset):
    with allure.step(f'Запрос списка (limit={limit}, offset={offset})'):
        response = api.get_types_list(limit, offset)
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
def test_404_for_invalid_type(api, check):
    with allure.step("Запрос несуществующего типа"):
        response = api.get_type_by_name('non_existent_type')
        with allure.step('Проверка статус-кода ответа'):
            check.status_code(response, 404)
