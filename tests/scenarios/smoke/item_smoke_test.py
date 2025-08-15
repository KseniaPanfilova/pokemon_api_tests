import pytest
import allure

ITEM_NAMES = [
    pytest.param('safari-ball', id='Safari-ball'),
    pytest.param('potion', id='Potion'),
    pytest.param('burn-heal', id='Burn-heal')
]

ITEM_IDS = [
    pytest.param(5, 'safari-ball', id='5'),
    pytest.param(17, 'potion', id='17'),
    pytest.param(19, 'burn-heal', id='19')
]

LIST_PARAMS = [
    pytest.param(1, 0, id='1_item'),
    pytest.param(5, 0, id='5_items'),
    pytest.param(10, 5, id='10_items_offset_5')
]


@pytest.mark.smoke
@pytest.mark.parametrize('item_name', ITEM_NAMES)
@allure.description('Проверка получения предмета по названию.\n'
                    'Цель: убедиться, что можно получить предмет по названию.')
def test_get_item_by_name(api, checker, item_name):
    with allure.step(f'Запрос предмета "{item_name}"'):
        response = api.get_item_by_name(item_name)
        with allure.step('Проверка статус-кода ответа'):
            checker.status_code(response, 200)
        with allure.step(f'Проверка, что в ответе приходит предмет "{item_name}"'):
            checker.json_value(response, field_name='name', expected_value=item_name)


@pytest.mark.smoke
@pytest.mark.parametrize('item_id, item_name', ITEM_IDS)
@allure.description('Тест получения предмета по ID.\n'
                    'Цель: убедиться, что можно получить данные о предмете по его ID.')
def test_get_item_by_id(api, checker, item_id, item_name):
    with allure.step(f'Запрос предмет c ID "{item_id}"'):
        response = api.get_item_by_id(item_id)
        with allure.step('Проверка статус-кода ответа'):
            checker.status_code(response, 200)
        with allure.step(f'Проверка, что в ответе приходит предмет "{item_name}"'):
            checker.json_value(response, field_name='name', expected_value=item_name)


@pytest.mark.smoke
@pytest.mark.parametrize('limit, offset', LIST_PARAMS)
@allure.description('Тест получения списка предметов.\n'
                    'Проверить, что список предметов можно ограничить.')
def test_get_items_list(api, checker, limit, offset):
    with allure.step(f'Запрос списка (limit={limit}, offset={offset})'):
        response = api.get_items_list(limit, offset)
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
def test_404_for_invalid_item(api, checker):
    with allure.step("Запрос несуществующего предмета"):
        response = api.get_item_by_name('non_existent_item')
        with allure.step('Проверка статус-кода ответа'):
            checker.status_code(response, 404)
