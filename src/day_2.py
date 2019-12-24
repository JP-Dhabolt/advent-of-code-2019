from typing import List

program_map = {1: lambda i1, i2: str(i1 + i2), 2: lambda i1, i2: str(i1 * i2)}


def run_program(registers: List[str]) -> List[str]:
    program_register = 0
    while program_register < len(registers):
        program_code = int(registers[program_register])
        if program_code == 99:
            return registers
        input1 = int(registers[program_register + 1])
        input2 = int(registers[program_register + 2])
        output = int(registers[program_register + 3])
        registers[output] = program_map[program_code](
            int(registers[input1]), int(registers[input2])
        )
        program_register += 4
