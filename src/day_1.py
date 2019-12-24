from typing import List


def calculate_fuel(masses: List) -> int:
    fuel = 0
    for mass in masses:
        fuel += int(mass / 3) - 2
    return fuel


def calculate_actual_fuel(masses: List) -> int:
    fuel = 0
    for mass in masses:
        interim_fuel = int(mass / 3) - 2
        additional_fuel = (
            0 if interim_fuel < 6 else calculate_actual_fuel([interim_fuel])
        )
        fuel += interim_fuel + additional_fuel
    return fuel
