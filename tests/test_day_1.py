from pytest import mark

from .resources import inputs
from src.day_1 import calculate_fuel


@mark.parametrize(
    "test_input,expected", [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
)
def test_calculate_fuel_with_provided(test_input, expected):
    actual = calculate_fuel([test_input])
    assert expected == actual


def test_calculate_fuel_for_answer():
    print(calculate_fuel(inputs.advent_1_input))
