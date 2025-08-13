from tests.base_test import BaseTest


class TestItems(BaseTest):

    def get_item_by_name_test(self, item_name: str = None) -> dict:
        """
        Проверка получения предмета по названию.
        Цель: убедиться, что можно получить предмет по названию.
        :param item_name: Название предмета (обязательный)
        :return: Данные о предмете
        """
        response = self.pokemon_api.get_item_by_name_or_id(item_name)
        self.check.status_code(response, 200)
        self.check.json_value(response, field_name='name', expected_value=item_name)
        return response.json()

    def get_item_by_id_test(self, item_id: int = None, expected_item_name: str = None) -> dict:
        """
        Проверка получения предмета по ID.
        Цель: убедиться, что можно получить предмет по ID.
        :param item_id: ID предмета (обязательный)
        :param expected_item_name: Ожидаемое название предмета (обязательный)
        :return: Данные о предмете
        """
        response = self.pokemon_api.get_item_by_name_or_id(item_id)
        self.check.status_code(response, 200)
        self.check.json_value(response, field_name='name', expected_value=expected_item_name)
        return response.json()

    def get_items_list(self, limit: int = None, offset: int = None) -> list[dict]:
        """
        Проверка получение списка предметов с лимитом.
        Цель: убедиться, что API возвращает ровно limit записей.
        :param limit: Количество записей, которые хотим получить (обязательный)
        :param offset: (опциональный)
        :return: Список с данными о предметах.
        """
        response = self.pokemon_api.get_items_list(limit, offset)
        self.check.status_code(response, 200)
        self.check.elements_count(response, limit - offset)
        return response.json()

    def get_non_existent_item_test(self) -> None:
        """
        Проверка получение несуществующего предмета.
        Цель: убедиться, что API корректно обрабатывает ошибки.
        :return: None
        """
        response = self.pokemon_api.get_item_by_name_or_id('non_existent_item')
        self.check.status_code(response, 404)
