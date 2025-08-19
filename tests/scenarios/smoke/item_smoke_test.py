import pytest
import allure
from data.test_data.item_data import ITEM_IDS, ITEM_NAMES, LIST_PARAMS

@pytest.mark.smoke
@pytest.mark.parametrize('item_name', ITEM_NAMES)
@allure.description('Проверка получения предмета по названию.\n'
                    'Цель: убедиться, что можно получить предмет по названию.')
def test_get_item_by_name(api, check, item_name):
    with allure.step(f'Запрос предмета "{item_name}"'):
        response = api.get_item_by_name(item_name)
        with allure.step('Проверка статус-кода ответа'):
            check.status_code(response, 200)
        with allure.step(f'Проверка, что в ответе приходит предмет "{item_name}"'):
            check.json_value(response, field_name='name', expected_value=item_name)


@pytest.mark.smoke
@pytest.mark.parametrize('item_id, item_name', ITEM_IDS)
@allure.description('Тест получения предмета по ID.\n'
                    'Цель: убедиться, что можно получить данные о предмете по его ID.')
def test_get_item_by_id(api, check, item_id, item_name):
    with allure.step(f'Запрос предмет c ID "{item_id}"'):
        response = api.get_item_by_id(item_id)
        with allure.step('Проверка статус-кода ответа'):
            check.status_code(response, 200)
        with allure.step(f'Проверка, что в ответе приходит предмет "{item_name}"'):
            check.json_value(response, field_name='name', expected_value=item_name)


@pytest.mark.smoke
@pytest.mark.parametrize('limit, offset', LIST_PARAMS)
@allure.description('Тест получения списка предметов.\n'
                    'Проверить, что список предметов можно ограничить.')
def test_get_items_list(api, check, limit, offset):
    with allure.step(f'Запрос списка (limit={limit}, offset={offset})'):
        response = api.get_items_list(limit, offset)
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
def test_404_for_invalid_item(api, check):
    with allure.step("Запрос несуществующего предмета"):
        response = api.get_item_by_name('non_existent_item')
        with allure.step('Проверка статус-кода ответа'):
            check.status_code(response, 404)
