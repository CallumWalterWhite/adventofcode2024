from util.input import get_input_as_list
import functools

@functools.lru_cache(maxsize=None)
def single_blink_stone(value):
    text = str(value)
    num_of_digits = len(text)
    if value == 0:
        return (1, None)
    elif num_of_digits % 2 == 0:
        mid_point = num_of_digits // 2
        left_stone = int(text[:mid_point])
        right_stone = int(text[mid_point:])

        return (left_stone, right_stone)
    
    else:
        return (value * 2024, None)

@functools.lru_cache(maxsize=None)
def count_stone_blinks(stone, depth):
    left_stone, right_stone = single_blink_stone(stone)
    if depth == 1:
        if right_stone is None:
            return 1
        else:
            return 2
    else:
        output = count_stone_blinks(left_stone, depth - 1)
        if right_stone is not None:
            output += count_stone_blinks(right_stone, depth - 1)
        return output
    
if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_11.txt")[0]
    result_75 = 0
    result_25 = 0
    for stone in input_data:
        result_75 += count_stone_blinks(int(stone), 75)
        result_25 += count_stone_blinks(int(stone), 25)
    
    print(result_25) # part 1
    print(result_75) # part 2