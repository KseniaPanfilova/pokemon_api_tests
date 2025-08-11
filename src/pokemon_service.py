from src.api_client import HttpClient


class PokemonAPI(HttpClient):

    def get_pokemon_by_name_or_id(self, pokemon_name_or_id: str | int):
        return self.get(endpoint=f'pokemon/{pokemon_name_or_id}')

    def get_pokemon_list(self, limit: int, offset: int):
        return self.get(endpoint='pokemon', params={'limit': limit, 'offset': offset})

    def get_ability_by_name_or_id(self, ability_name_or_id: str | int):
        return self.get(endpoint=f'ability/{ability_name_or_id}')

    def get_ability_list(self, limit: int, offset: int):
        return self.get(endpoint='ability', params={'limit': limit, 'offset': offset})

    def get_type_by_name_or_id(self, type_name_or_id: str | int):
        return self.get(endpoint=f'type/{type_name_or_id}')

    def get_type_list(self):
        return self.get(endpoint='type')

    def get_move_by_name_or_id(self, move_name_oe_id: str | int):
        return self.get(endpoint=f'move/{move_name_oe_id}')

    def get_move_list(self, limit: int, offset: int):
        return self.get(endpoint='move', params={'limit': limit, 'offset': offset})

    def get_item_by_name_or_id(self, item_name_oe_id: str | int):
        return self.get(endpoint=f'item/{item_name_oe_id}')

    def get_item_list(self, limit: int, offset: int):
        return self.get(endpoint='item', params={'limit': limit, 'offset': offset})

    def get_pokemon_species_by_name_or_id(self, pokemon_species_name_oe_id: str | int):
        return self.get(endpoint=f'pokemon-species/{pokemon_species_name_oe_id}')

    def get_pokemon_species_list(self, limit: int, offset: int):
        return self.get(endpoint='pokemon-species', params={'limit': limit, 'offset': offset})
