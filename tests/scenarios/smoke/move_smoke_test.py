import pytest
import allure

MOVE_NAMES = [
    pytest.param('bind', id='Bind'),
    pytest.param('swords-dance', id='Swords-dance'),
    pytest.param('pay-day', id='Pay-day')
]

MOVE_IDS = [
    pytest.param(20, 'bind', id='20'),
    pytest.param(14, 'swords-dance', id='14'),
    pytest.param(6, 'pay-day', id='6')
]

LIST_PARAMS = [
    pytest.param(1, 0, id='1_move'),
    pytest.param(5, 0, id='5_moves'),
    pytest.param(10, 5, id='10_moves_offset_5')
]


@pytest.mark.smoke
@pytest.mark.parametrize('move_name', MOVE_NAMES)
@allure.description('Проверка получения движения по названию.\n'
                    'Цель: убедиться, что можно получить движение по названию.')
def test_get_move_by_name(api, check, move_name):
    with allure.step(f'Запрос движения "{move_name}"'):
        response = api.get_move_by_name(move_name)
        with allure.step('Проверка статус-кода ответа'):
            check.status_code(response, 200)
        with allure.step(f'Проверка, что в ответе приходит движение "{move_name}"'):
            check.json_value(response, field_name='name', expected_value=move_name)


@pytest.mark.smoke
@pytest.mark.parametrize('move_id, move_name', MOVE_IDS)
@allure.description('Тест получения движения по ID.\n'
                    'Цель: убедиться, что можно получить данные о движении по его ID.')
def test_get_move_by_id(api, check, move_id, move_name):
    with allure.step(f'Запрос движения c ID "{move_id}"'):
        response = api.get_move_by_id(move_id)
        with allure.step('Проверка статус-кода ответа'):
            check.status_code(response, 200)
        with allure.step(f'Проверка, что в ответе приходит движение "{move_name}"'):
            check.json_value(response, field_name='name', expected_value=move_name)


@pytest.mark.smoke
@pytest.mark.parametrize('limit, offset', LIST_PARAMS)
@allure.description('Тест получения списка движений.\n'
                    'Проверить, что список движений можно ограничить.')
def test_get_moves_list(api, check, limit, offset):
    with allure.step(f'Запрос списка (limit={limit}, offset={offset})'):
        response = api.get_moves_list(limit, offset)
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
def test_404_for_invalid_move(api, check):
    with allure.step("Запрос несуществующего движения"):
        response = api.get_move_by_name('non_existent_move')
        with allure.step('Проверка статус-кода ответа'):
            check.status_code(response, 404)