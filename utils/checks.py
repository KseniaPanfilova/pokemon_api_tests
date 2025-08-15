import json
from jsonschema import validate


class Checks:

    @staticmethod
    def status_code(response, status_code: int) -> None:
        """Метод для проверки статус кода"""
        assert response.status_code == status_code, (
            f'ОШИБКА, Статус-код {response.status_code} не совпадает с ожидаемым {status_code}.')
        print(f'Статус код = {response.status_code}')

    @staticmethod
    def json_value(response, field_name: str = None, expected_value: str | int | bool = None) -> None:
        """Метод для проверки значений полей в ответе запроса"""

        check = response.json()

        if isinstance(check, str):
            assert check == expected_value, f'ОШИБКА, ответ {check} не совпадает с ожидаемым: {expected_value}.'
            print(check)
            print('Ответ верный!')
            return

        check_info = check
        for key in field_name.split('.'):
            if isinstance(check_info, dict):
                check_info = check_info.get(key)
            elif isinstance(check_info, list):
                check_info = check_info[int(key)]

        assert check_info == expected_value, (f'ОШИБКА, значение поля {check_info} не совпадает с ожидаемым '
                                              f'{expected_value}.')
        print(check_info)
        print(f'Значение {field_name} верно!')

    @staticmethod
    def data_type(response, field_name: str = None, expected_type: str = None) -> None:
        """Метод для проверки соответствия типа данных"""
        assert isinstance(response.json()[field_name], expected_type), (f'ОШИБКА, значение поля {field_name} '
                                                                        f'не соответсвует ожидаемому типу данных '
                                                                        f'{expected_type}')
        print(type(response.json()[field_name]))
        print(f'Тип поля {field_name} верный - {expected_type}.')

    @staticmethod
    def json_schema(response, schema: dict = None) -> None:
        """Метод для валидации json-схемы"""
        data = response.json()
        assert validate(instance=data, schema=schema), 'ОШИБКА валидации'
        print("JSON соответствует схеме")

    @staticmethod
    def elements_count(response, expected_count: int) -> None:
        """Метод для проверки количества элементов в списке"""
        results_count = len(response.json()['results'])
        assert results_count == expected_count, f'ОШИБКА, количество элементов в списке {results_count}'
        f'не совпадает с ожидаемым результатом {expected_count}.'
        print(results_count)
        print(f'Количество результатов - {results_count}.')

    @staticmethod
    def offset(response, expected_offset: int, limit: int) -> None:
        """Метод для проверки применения параметра offset"""
        assert (f'offset={expected_offset + limit}' in response.json()['next']
                and 'offset=0' in response.json()['previous']), f'ОШИБКА, размер офсета не совпадает с ожидаемым.'
        print(response.json()['next'])
        print(response.json()['previous'])
        assert response.json()['results'][0]['url'][-2] == str(expected_offset + 1), \
            f'ОШИБКА, размер офсета не совпадает с ожидаемым.'
        print(f"ID первого элемента в списке - {response.json()['results'][0]['url'][-2]}")
        print('Офсет применен верно.')
