from tests.base_test import BaseTest


class TestMoves(BaseTest):

    def get_move_by_name_test(self, move_name: str = None) -> dict:
        """
        Проверка получения движения по названию.
        Цель: убедиться, что можно получить движение по названию.
        :param move_name: Название движения (обязательный)
        :return: Данные о движении
        """
        response = self.pokemon_api.get_move_by_name_or_id(move_name)
        self.check.status_code(response, 200)
        self.check.json_value(response, field_name='name', expected_value=move_name)
        return response.json()

    def get_move_by_id_test(self, move_id: int = None, expected_move_name: str = None) -> dict:
        """
        Проверка получения движения по ID.
        Цель: убедиться, что можно получить движение по ID.
        :param move_id: ID движения (обязательный)
        :param expected_move_name: Ожидаемое название движения (обязательный)
        :return: Данные о движении
        """
        response = self.pokemon_api.get_move_by_name_or_id(move_id)
        self.check.status_code(response, 200)
        self.check.json_value(response, field_name='name', expected_value=expected_move_name)
        return response.json()

    def get_moves_list(self, limit: int = None, offset: int = None) -> list[dict]:
        """
        Проверка получение списка движений с лимитом.
        Цель: убедиться, что API возвращает ровно limit записей.
        :param limit: Количество записей, которые хотим получить (обязательный)
        :param offset: (опциональный)
        :return: Список с данными о движениях.
        """
        response = self.pokemon_api.get_moves_list(limit, offset)
        self.check.status_code(response, 200)
        self.check.elements_count(response, limit - offset)
        return response.json()

    def get_non_existent_move_test(self) -> None:
        """
        Проверка получение несуществующего движения.
        Цель: убедиться, что API корректно обрабатывает ошибки.
        :return: None
        """
        response = self.pokemon_api.get_move_by_name_or_id('non_existent_move')
        self.check.status_code(response, 404)
