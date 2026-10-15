import pytest

from bun import Bun


@pytest.mark.parametrize(
    "name",
    [
        "black bun",
        "white bun",
        "red bun",
    ],
)
def test_get_name(name):
    bun = Bun(name, 100)

    assert bun.get_name() == name


@pytest.mark.parametrize(
    "price",
    [
        100,
        200,
        300,
    ],
)
def test_get_price(price):
    bun = Bun("black bun", price)

    assert bun.get_price() == price