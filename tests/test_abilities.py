from tests.base_test import BaseTest


class TestAbilities(BaseTest):

    def get_ability_by_name_test(self, ability_name: str = None) -> dict:
        """
        Проверка получения способности по названию.
        Цель: убедиться, что можно получить данные о способности по ее названию.
        :param ability_name: Название способности (обязательный)
        :return: Данные о способности
        """
        response = self.pokemon_api.get_ability_by_name_or_id(ability_name)
        self.check.status_code(response, 200)
        self.check.json_value(response, field_name='name', expected_value=ability_name)
        return response.json()

    def get_ability_by_id_test(self, ability_id: int = None, expected_ability_name: str = None) -> dict:
        """
        Проверка получения способности по названию.
        Цель: убедиться, что можно получить данные о способности по ее ID.
        :param ability_id: ID способности (обязательный)
        :param expected_ability_name: Ожидаемое название способности (обязательный)
        :return: Данные о способности
        """
        response = self.pokemon_api.get_ability_by_name_or_id(ability_id)
        self.check.status_code(response, 200)
        self.check.json_value(response, field_name='name', expected_value=expected_ability_name)
        return response.json()

    def get_abilities_list_test(self, limit: int = None, offset: int = 0) -> list[dict]:
        """
        Проверка получения списка способностей с лимитом.
        Цель: проверить, что список способностей можно ограничить.
        :param limit: Количество записей, которые хотим получить (обязательный)
        :param offset: (опциональный)
        :return: Список с данными о способностях
        """
        response = self.pokemon_api.get_abilities_list(limit, offset)
        self.check.status_code(response, 200)
        self.check.elements_count(response, limit - offset)
        return response.json()

    def get_non_existent_ability_test(self) -> None:
        """
        Проверка получение несуществующей способности.
        Цель: убедиться, что API корректно обрабатывает ошибки.
        :return: None
        """
        response = self.pokemon_api.get_ability_by_name_or_id('non_existent_ability')
        self.check.status_code(response, 404)