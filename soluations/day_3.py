from util.input import get_input_as_string
import re

def parse_mul_instructions(input_data, handle_do_dont=False):
    mul_pattern = r'mul\((\d+),(\d+)\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    total_mul = 0
    is_enabled = True if handle_do_dont else True
    
    mul_matches = re.finditer(mul_pattern, input_data)
    
    if handle_do_dont:
        do_matches = list(re.finditer(do_pattern, input_data))
        dont_matches = list(re.finditer(dont_pattern, input_data))
        
        all_matches = sorted(
            list(mul_matches) + list(do_matches) + list(dont_matches), 
            key=lambda x: x.start()
        )
        
        for match in all_matches:
            if match.group(0) == 'do()':
                is_enabled = True
            elif match.group(0) == 'don\'t()':
                is_enabled = False
            elif match.group(0).startswith('mul('):
                if is_enabled:
                    x, y = map(int, match.groups())
                    total_mul += x * y
    else:
        for match in mul_matches:
            x, y = map(int, match.groups())
            total_mul += x * y
    
    return total_mul

def part_1(input_data):
    return parse_mul_instructions(input_data)

def part_2(input_data):
    return parse_mul_instructions(input_data, handle_do_dont=True)

if __name__ == "__main__":
    input_data = get_input_as_string("inputs/day_3.txt")
    input_data_part_2 = get_input_as_string("inputs/day_3_part_2.txt")
    print(part_1(input_data))
    print(part_2(input_data_part_2))