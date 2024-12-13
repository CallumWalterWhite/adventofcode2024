from util.input import get_input_as_list

def count_x_mas(matrix_data):
    max_y, max_x = len(matrix_data), len(matrix_data[0])
    total_count = 0
    word = "MAS"
    reversed_word = word[::-1]
    def is_valid_diagonal(x, y, dx, dy):
        sequence = []
        for i in range(3): 
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < max_x and 0 <= ny < max_y):
                return False
            sequence.append(matrix_data[ny][nx])
        return "".join(sequence) == word or "".join(sequence) == reversed_word

    for y in range(1, max_y - 1): 
        for x in range(1, max_x - 1):  
            if (is_valid_diagonal(x - 1, y - 1, 1, 1) and  
                is_valid_diagonal(x + 1, y - 1, -1, 1)):  
                total_count += 1

    return total_count

if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_4.txt")
    word = "XMAS"
    matrix_data = [x[0] for x in input_data]
    max_y, max_x = len(matrix_data), len(matrix_data[0])
    word_len = len(word)
    total_count = 0

    directions = [
        (1, 0),   # right
        (0, 1),   # down
        (-1, 0),  # left
        (0, -1),  # up
        (1, 1),   # down-right
        (-1, -1), # up-left
        (1, -1),  # up-right
        (-1, 1)   # down-left
    ]

    def matches_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < max_x and 0 <= ny < max_y):
                return False
            if matrix_data[ny][nx] != word[i]:
                return False
        return True

    for y in range(max_y):
        for x in range(max_x):
            for dx, dy in directions:
                if matches_from(x, y, dx, dy):
                    total_count += 1
    print(total_count)
    print(count_x_mas(matrix_data))