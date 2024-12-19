import math
from util.input import get_input_as_list
    
def parse_input_data(input_data):
    registers = {
        "A": 0,
        "B": 0,
        "C": 0,
    }
    for line in [l for l in input_data if len(l) > 0]:
        char = line[1]
        for register in registers:
            if register in char:
                registers[register] = int(line[2])
                continue
    return (registers, [int(l) for l in line[-1].split(",")])    
    
def run_program(registers, program):
    def get_operand_value(operand):
        operands_pointer = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: registers["A"],
            5: registers["B"],
            6: registers["C"]
        }
        return operands_pointer[operand]
    
    def adv(operand):
        registers["A"] = math.trunc(registers["A"] / (2 ** get_operand_value(operand)))
        return 2
        
    def bxl(operand):
        registers["B"] = registers["B"] ^ operand
        return 2
    
    def bst(operand):
        registers["B"] = get_operand_value(operand) % 8
        return 2
    
    def bxc(operand):
        registers["B"] = registers["B"] ^ registers["C"]
        return 2
    
    def out(operand):
        value = get_operand_value(operand) % 8
        return [c for c in str(value)]
    
    def bdv(operand):
        registers["B"] = math.trunc(registers["A"] / (2 ** get_operand_value(operand)))
        return 2
    
    def cdv(operand):
        registers["C"] = math.trunc(registers["A"] / (2 ** get_operand_value(operand)))
        return 2
    
    operation_map = {
        0: adv,
        1: bxl,
        2: bst,
        3: None,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv
    }
    output = []
    pi = 0
    while pi < len(program):
        opcode = program[pi]
        operation = operation_map[opcode]
        if pi + 1 >= len(program):
            break
        operand = program[pi + 1]
        if opcode == 5:
            output.extend(operation(operand))
            pi += 2
        elif opcode == 3:
            if registers["A"] == 0:
                pi += 2
            else:
                pi = operand
        else:
            pi += operation(operand)
    return output
    
if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_17.txt")
    registers, program = parse_input_data(input_data)
    p2_registers = registers.copy()
    print(",".join(run_program(registers, program))) # part 1
    
    # p2_registers["A"] = 1
    # program_output = ""
    # cur_A = p2_registers["A"]
    # str_program = ",".join([str(p) for p in program])
    # while (program_output != str_program):
    #     print(p2_registers["A"])
    #     run_program_registers = p2_registers.copy()
    #     program_output = ",".join(run_program(run_program_registers, program))
    #     p2_registers["A"] = p2_registers["A"] + 1
    # print(p2_registers["A"] - 1)