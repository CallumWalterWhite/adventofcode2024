from util.input import get_input_as_list
from operator import add, mul

# 190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20

if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_7.txt")
    operations_map = {}
    for ops in input_data:
        total = int(ops[0][:-1])  
        operations_map[total] = [int(x) for x in ops[1:]]
    def check(array, res, part):
        def concat(a, b):
            return int(f"{a}{b}")
        operators = (add, mul) if part == 1 else (add, mul, concat)
        memo = {0}
        for n in array:
            memo = {op(last_result, n) for last_result in memo for op in operators}
        return array if res in memo else False
    sum_part1 = sum(
        target for target, values in operations_map.items()
        if check(values, target, part=1)
    )
    sum_part2 = sum(
        target for target, values in operations_map.items()
        if check(values, target, part=2)
    )
    print(f"Part 1: {sum_part1}")
    print(f"Part 2: {sum_part2}")