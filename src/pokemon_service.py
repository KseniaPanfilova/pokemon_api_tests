import requests

from src.api_client import HttpClient


class PokemonAPI(HttpClient):

    def get_resource(self, resource: str, id_or_name=None, params=None, headers=None):
        """
        Универсальный метод получения ресурса.
        :param resource: Имя ресурса (например, 'pokemon', 'ability', 'type')
        :param id_or_name: ID или имя конкретного объекта (необязательно)
        :param params: GET-параметры
        :param headers: Заголовки
        """
        endpoint = f"/{resource}"
        if id_or_name is not None:
            endpoint += f"/{id_or_name}"
        return self.get(endpoint=endpoint, params=params, headers=headers)

    def get_pokemon_by_name(self, pokemon_name: str) -> requests.Response:
        """
        Метод для получения покемона по названию.
        :param pokemon_name: Название покемона
        """
        return self.get_resource('pokemon', id_or_name=pokemon_name)

    def get_pokemon_by_id(self, pokemon_id: int) -> requests.Response:
        """
        Метод для получения покемона по ID.
        :param pokemon_id: ID покемона
        """
        return self.get_resource('pokemon', id_or_name=pokemon_id)

    def get_pokemons_list(self, limit: int = 0, offset: int = 0) -> requests.Response:
        """
        Метод для получения списка покемонов.
        :param limit: Количество элементов списка
        :param offset: Пропускаемое количество элементов от начала полного списка
        """
        return self.get_resource('pokemon', params={'limit': limit, 'offset': offset})

    def get_ability_by_name(self, ability_name: str) -> requests.Response:
        """
        Метод для получения способности по названию.
        :param ability_name: Название способности
        """
        return self.get_resource('ability', id_or_name=ability_name)

    def get_ability_by_id(self, ability_id: int) -> requests.Response:
        """
        Метод для получения способности по ID.
        :param ability_id: ID способности
        """
        return self.get_resource('ability', id_or_name=ability_id)

    def get_abilities_list(self, limit: int = 0, offset: int = 0) -> requests.Response:
        """
        Метод для получения списка способностей.
        :param limit: Количество элементов списка
        :param offset: Пропускаемое количество элементов от начала полного списка
        """
        return self.get_resource('ability', params={'limit': limit, 'offset': offset})

    def get_type_by_name(self, type_name: str) -> requests.Response:
        """
        Метод для получения типа по названию.
        :param type_name: Название типа
        """
        return self.get_resource('type', id_or_name=type_name)

    def get_type_by_id(self, type_id: int) -> requests.Response:
        """
        Метод для получения типа по ID.
        :param type_id: ID типа
        """
        return self.get_resource('type', id_or_name=type_id)

    def get_types_list(self, limit: int = 0, offset: int = 0) -> requests.Response:
        """
        Метод для получения списка типов.
        :param limit: Количество элементов списка
        :param offset: Пропускаемое количество элементов от начала полного списка
        """
        return self.get_resource('type', params={'limit': limit, 'offset': offset})

    def get_move_by_name(self, move_name: str) -> requests.Response:
        """
        Метод для получения движения по названию.
        :param move_name: Название движения
        """
        return self.get_resource('move', id_or_name=move_name)

    def get_move_by_id(self, move_id: int) -> requests.Response:
        """
        Метод для получения движения по ID.
        :param move_id: ID движения
        """
        return self.get_resource('move', id_or_name=move_id)

    def get_moves_list(self, limit: int, offset: int) -> requests.Response:
        """
        Метод для получения списка движений.
        :param limit: Количество элементов списка
        :param offset: Пропускаемое количество элементов от начала полного списка
        """
        return self.get_resource('move', params={'limit': limit, 'offset': offset})

    def get_item_by_name(self, item_name: str) -> requests.Response:
        """
        Метод для получения предмета по названию.
        :param item_name: Название предмета
        """
        return self.get_resource('item', id_or_name=item_name)

    def get_item_by_id(self, item_id: int) -> requests.Response:
        """
        Метод для получения предмета по ID.
        :param item_id: ID предмета
        """
        return self.get_resource('item', id_or_name=item_id)

    def get_items_list(self, limit: int, offset: int) -> requests.Response:
        """
        Метод для получения списка предметов.
        :param limit: Количество элементов списка
        :param offset: Пропускаемое количество элементов от начала полного списка
        """
        return self.get_resource('item', params={'limit': limit, 'offset': offset})
