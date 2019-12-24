from typing import List


def calculate_fuel(masses: List) -> int:
    fuel = 0
    for mass in masses:
        fuel += int(mass / 3) - 2
    return fuel
