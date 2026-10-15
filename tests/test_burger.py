import pytest

from burger import Burger


class TestBurger:
    def test_set_buns(self, create_bun):
        burger = Burger()
        bun = create_bun()

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self, create_ingredient):
        burger = Burger()
        ingredient = create_ingredient()

        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self, create_ingredient):
        burger = Burger()
        first_ingredient = create_ingredient(name="first")
        second_ingredient = create_ingredient(name="second")

        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == [second_ingredient]

    @pytest.mark.parametrize(
        "index, new_index, expected",
        [
            (0, 1, ["second", "first", "third"]),
            (2, 0, ["third", "first", "second"]),
            (1, 2, ["first", "third", "second"]),
        ],
    )
    def test_move_ingredient(self, index, new_index, expected):
        burger = Burger()
        burger.ingredients = ["first", "second", "third"]

        burger.move_ingredient(index, new_index)

        assert burger.ingredients == expected

    def test_get_price(self, create_bun, create_ingredient):
        burger = Burger()
        bun = create_bun(price=100)
        ingredient_1 = create_ingredient(price=50)
        ingredient_2 = create_ingredient(price=30)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        assert burger.get_price() == 280

    def test_get_receipt(self, create_bun, create_ingredient):
        burger = Burger()
        bun = create_bun(name="black bun", price=100)
        ingredient = create_ingredient(
            ingredient_type="SAUCE",
            name="hot sauce",
            price=50,
        )

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_receipt() == (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "Price: 250"
        )