import pytest

from database import Database
from ingredient_types import (
    INGREDIENT_TYPE_FILLING,
    INGREDIENT_TYPE_SAUCE,
)


def test_available_buns():
    database = Database()

    buns = database.available_buns()

    assert [
        (bun.get_name(), bun.get_price())
        for bun in buns
    ] == [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ]


@pytest.mark.parametrize(
    "index, ingredient_type, name, price",
    [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
    ],
)
def test_available_ingredients(index, ingredient_type, name, price):
    database = Database()

    ingredient = database.available_ingredients()[index]

    assert (
        ingredient.get_type(),
        ingredient.get_name(),
        ingredient.get_price(),
    ) == (ingredient_type, name, price)