from tests.base_test import BaseTest


class TestPokemons(BaseTest):

    def get_pokemon_by_name_test(self, pokemon_name: str = None) -> dict:
        """
        Проверка получения покемона по названию.
        Цель: убедиться, что можно получить данные о покемоне по ее названию.
        :param pokemon_name: Название покемона (обязательный)
        :return: Данные о покемоне
        """
        response = self.pokemon_api.get_pokemon_by_name_or_id(pokemon_name)
        self.check.status_code(response, 200)
        self.check.json_value(response, field_name='name', expected_value=pokemon_name)
        return response.json()

    def get_pokemon_by_id_test(self, pokemon_id: int = None, expected_pokemon_name: str = None) -> dict:
        """
        Проверка получения покемона по названию.
        Цель: убедиться, что можно получить данные о покемоне по ее ID.
        :param pokemon_id: ID покемона (обязательный)
        :param expected_pokemon_name: Ожидаемое название покемона (обязательный)
        :return: Данные о покемоне
        """
        response = self.pokemon_api.get_pokemon_by_name_or_id(pokemon_id)
        self.check.status_code(response, 200)
        self.check.json_value(response, field_name='name', expected_value=expected_pokemon_name)
        return response.json()

    def get_pokemons_list_test(self, limit: int = None, offset: int = 0) -> list[dict]:
        """
        Проверка получения списка покемонов с лимитом.
        Цель: проверить, что список покемонов можно ограничить.
        :param limit: Количество записей, которые хотим получить (обязательный)
        :param offset: (опциональный)
        :return: Список с данными о покемонах
        """
        response = self.pokemon_api.get_pokemons_list(limit, offset)
        self.check.status_code(response, 200)
        self.check.elements_count(response, limit)
        return response.json()

    def get_non_existent_pokemon_test(self) -> None:
        """
        Проверка получение несуществующего покемона.
        Цель: убедиться, что API корректно обрабатывает ошибки.
        :return: None
        """
        response = self.pokemon_api.get_pokemon_by_name_or_id('non_existent_pokemon')
        self.check.status_code(response, 404)
