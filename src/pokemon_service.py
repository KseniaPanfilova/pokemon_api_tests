import requests

from src.api_client import HttpClient


class PokemonAPI(HttpClient):

    def get_pokemon_by_name_or_id(self, pokemon_name_or_id: str | int) -> requests.Response:
        return self.get(endpoint=f'pokemon/{pokemon_name_or_id}')

    def get_pokemons_list(self, limit: int, offset: int) -> requests.Response:
        return self.get(endpoint='pokemon', params={'limit': limit, 'offset': offset})

    def get_ability_by_name_or_id(self, ability_name_or_id: str | int) -> requests.Response:
        return self.get(endpoint=f'ability/{ability_name_or_id}')

    def get_abilities_list(self, limit: int, offset: int) -> requests.Response:
        return self.get(endpoint='ability', params={'limit': limit, 'offset': offset})

    def get_type_by_name_or_id(self, type_name_or_id: str | int) -> requests.Response:
        return self.get(endpoint=f'type/{type_name_or_id}')

    def get_types_list(self) -> requests.Response:
        return self.get(endpoint='type')

    def get_move_by_name_or_id(self, move_name_or_id: str | int) -> requests.Response:
        return self.get(endpoint=f'move/{move_name_or_id}')

    def get_moves_list(self, limit: int, offset: int) -> requests.Response:
        return self.get(endpoint='move', params={'limit': limit, 'offset': offset})

    def get_item_by_name_or_id(self, item_name_or_id: str | int) -> requests.Response:
        return self.get(endpoint=f'item/{item_name_or_id}')

    def get_items_list(self, limit: int, offset: int) -> requests.Response:
        return self.get(endpoint='item', params={'limit': limit, 'offset': offset})
