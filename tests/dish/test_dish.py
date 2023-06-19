from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction # noqa: F401, E261, E501
import pytest


def test_dish():
    dish_one = Dish('food', 3)
    assert dish_one.name == 'food'
    dish_two = Dish('food', 3)
    assert repr(dish_one) == "Dish('food', R$3.00)"
    assert repr(dish_one) != "Dish('food', R$2.00)"
    assert hash(dish_one) == hash(Dish('food', 3))
    assert hash(dish_one) != hash(Dish('food', 1))
    assert dish_one != Dish('food', 1)
    assert dish_one == Dish('food', 3)
    with pytest.raises(TypeError):
        Dish(3, 'food')
    with pytest.raises(ValueError):
        Dish('food', -3)

    ingrediente_frango = Ingredient('frango')
    ingrediente_creme_de_leite = Ingredient('creme de leite')
    dish_one.add_ingredient_dependency(ingrediente_frango, 1)
    dish_two.add_ingredient_dependency(ingrediente_frango, 3)
    assert dish_one.get_ingredients() == {Ingredient('frango')}
    assert dish_one.get_restrictions() == dish_two.get_restrictions()
    dish_two.add_ingredient_dependency(ingrediente_creme_de_leite, 3)
    assert dish_one.get_restrictions() != dish_two.get_restrictions()
