class BaseTest:
    def __init__(self, pokemon_api, check):
        """
        :param pokemon_api: Объект класса сервисных методов PokeAPI
        :param check: Объект класса проверок
        """
        self.pokemon_api = pokemon_api
        self.check = check
