from tests.base_test import BaseTest


class TestTypes(BaseTest):

    def get_type_by_name_test(self, type_name: str = None) -> dict:
        """
        Проверка получения типа покемонов по названию.
        :param type_name: Название типа (обязательный)
        :return: Данные о типе
        """
        response = self.pokemon_api.get_type_by_name_or_id(type_name)
        self.check.status_code(response, 200)
        self.check.json_value(response, field_name='name', expected_value=type_name)
        return response.json()

    def get_type_by_id_test(self, type_id: int = None, expected_type_name: str = None) -> dict:
        """
        Проверка получения типа покемонов по ID.
        Цель: убедиться, что можно получить тип покемонов по ID.
        :param type_id: ID типа покемонов (обязательный)
        :param expected_type_name: Ожидаемое название типа (обязательный)
        :return: Данные о типа
        """
        response = self.pokemon_api.get_type_by_name_or_id(type_id)
        self.check.status_code(response, 200)
        self.check.json_value(response, field_name='name', expected_value=expected_type_name)
        return response.json()

    def get_types_list_test(self, limit: int = None, offset: int = 0) -> list[dict]:
        """
        Проверка получение списка типов с лимитом.
        Цель: убедиться, что API возвращает ровно limit записей.
        :param limit: Количество записей, которые хотим получить (обязательный)
        :param offset: (опциональный)
        :return: Список с данными о типах.
        """
        response = self.pokemon_api.get_types_list()
        self.check.status_code(response, 200)
        self.check.elements_count(response, limit - offset)
        return response.json()

    def get_non_existent_type_test(self) -> None:
        """
        Проверка получение несуществующего типа.
        Цель: убедиться, что API корректно обрабатывает ошибки.
        :return: None
        """
        response = self.pokemon_api.get_type_by_name_or_id('non_existent_type')
        self.check.status_code(response, 404)
