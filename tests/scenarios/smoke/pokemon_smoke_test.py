import pytest
import allure

POKEMON_NAMES = [
    pytest.param("pikachu", id="Pikachu"),
    pytest.param("charizard", id="Charizard"),
    pytest.param("bulbasaur", id="Bulbasaur")
]

POKEMON_IDS = [
    pytest.param(25, "pikachu", id="25"),
    pytest.param(6, "charizard", id="6"),
    pytest.param(1, "bulbasaur", id="1")
]

LIST_PARAMS = [
    pytest.param(1, 0, id="1_pokemon"),
    pytest.param(5, 0, id="5_pokemons"),
    pytest.param(10, 5, id="10_pokemons_offset_5")
]


@pytest.mark.smoke
@pytest.mark.parametrize("pokemon_name", POKEMON_NAMES)
@allure.description('Тест получения покемона по имени')
def test_get_pokemon_by_name(pokemon_tester, pokemon_name):
    with allure.step(f"Запрос покемона '{pokemon_name}'"):
        pokemon_tester.get_pokemon_by_name_test(pokemon_name)


@pytest.mark.smoke
@pytest.mark.parametrize("pokemon_id, pokemon_name", POKEMON_IDS)
@allure.description('Тест получения покемона по ID')
def test_get_pokemon_by_id(pokemon_tester, pokemon_id, pokemon_name):
    with allure.step(f"Запрос покемона c ID '{pokemon_id}'"):
        pokemon_tester.get_pokemon_by_id_test(pokemon_id, pokemon_name)


@pytest.mark.smoke
@pytest.mark.parametrize("limit, offset", LIST_PARAMS)
@allure.description('Тест получения списка покемонов')
def test_get_pokemons_list(pokemon_tester, limit, offset):
    with allure.step(f"Запрос списка (limit={limit}, offset={offset})"):
        pokemon_tester.get_pokemons_list_test(limit, offset)


@pytest.mark.smoke
@allure.description('Тест обработки 404 ошибки')
def test_404_for_invalid_pokemon(pokemon_tester):
    with allure.step("Запрос несуществующего покемона"):
        pokemon_tester.get_non_existent_pokemon_test()
