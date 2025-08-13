import json


class Checks:

    @staticmethod
    def status_code(result, status_code: int):
        """Метод для проверки статус кода"""
        assert result.status_code == status_code, (
            f'ОШИБКА, Статус-код {result.status_code} не совпадает с ожидаемым {status_code}.')
        print(f'Статус код = {result.status_code}')

    @staticmethod
    def json_value(result, field_name: str = None, expected_value: str | int | bool = None):
        """Метод для проверки значений полей в ответе запроса"""

        check = result.json()

        if isinstance(check, str):
            assert check == expected_value, f'ОШИБКА, ответ "{check}" не совпадает с ожидаемым: "{expected_value}".'
            print(check)
            print('Ответ верный!')
            return

        check_info = check
        for key in field_name.split('.'):
            if isinstance(check_info, dict):
                check_info = check_info.get(key)
            elif isinstance(check_info, list):
                check_info = check_info[int(key)]

        assert check_info == expected_value, f'ОШИБКА, значение поля "{check_info}" не совпадает с ожидаемым "{expected_value}".'
        print(check_info)
        print(f'Значение {field_name} верно!')

    @staticmethod
    def elements_count(response, expected_count: int):
        """Метод для проверки количества элементов в списке"""
        results_count = len(response.json()['results'])
        assert results_count == expected_count, f'ОШИБКА, количество элементов в списке {results_count}'
        f'не совпадает с ожидаемым результатом {expected_count}.'
        print(results_count)
        print(f'Количество результатов - {results_count}.')
