from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


def test_ingredient():
    ingrediente_frango = Ingredient('frango')

    assert ingrediente_frango.name == 'frango'
    assert ingrediente_frango.name != 'creme de leite'
    assert Restriction.ANIMAL_MEAT in ingrediente_frango.restrictions
    assert Restriction.ANIMAL_DERIVED in ingrediente_frango.restrictions
    assert Restriction.GLUTEN not in ingrediente_frango.restrictions
    assert Restriction.SEAFOOD not in ingrediente_frango.restrictions
    assert ingrediente_frango.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    assert ingrediente_frango.restrictions != {
        Restriction.GLUTEN,
        Restriction.SEAFOOD,
    }

    assert hash(ingrediente_frango) == hash('frango')
    assert hash(ingrediente_frango) != hash('creme de leite')
    assert repr(ingrediente_frango) == "Ingredient('frango')"
    assert repr(ingrediente_frango) != "Ingredient('creme de leite')"
    assert ingrediente_frango == Ingredient('frango')
    assert ingrediente_frango != Ingredient('creme de leite')
