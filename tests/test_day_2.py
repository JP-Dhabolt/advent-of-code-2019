from pytest import mark

from .resources.inputs import advent_2_input
from src.day_2 import run_program


@mark.parametrize(
    "test_input,expected",
    [
        ("1,0,0,0,99", "2,0,0,0,99"),
        ("2,3,0,3,99", "2,3,0,6,99"),
        ("2,4,4,5,99,0", "2,4,4,5,99,9801"),
        ("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99"),
    ],
)
def test_run_program_with_provided(test_input, expected):
    actual = run_program(test_input.split(","))
    assert ",".join(actual) == expected


def test_run_program_for_answer():
    advent_2_registers = advent_2_input.split(",")
    advent_2_registers[1] = "12"
    advent_2_registers[2] = "2"
    answer = run_program(advent_2_registers)
    print(answer[0])
