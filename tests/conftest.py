from unittest.mock import Mock

import pytest


@pytest.fixture
def create_bun():
    def _create_bun(name="black bun", price=100):
        bun = Mock()
        bun.get_name.return_value = name
        bun.get_price.return_value = price
        return bun

    return _create_bun


@pytest.fixture
def create_ingredient():
    def _create_ingredient(
        ingredient_type="SAUCE",
        name="hot sauce",
        price=50,
    ):
        ingredient = Mock()
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        return ingredient

    return _create_ingredient