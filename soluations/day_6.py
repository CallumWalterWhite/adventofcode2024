from util.input import get_input_as_list

# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...

if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_6.txt")
    matrix_data = [x[0] for x in input_data]
    max_y = len(matrix_data)
    max_x = len(matrix_data[0]) 
    print(max_x, max_y)
    
    pos_mov = 'up'
    
    start_x = -1
    start_y = -1
    
    obstacles=set()
    for y in range(max_y):
        for x in range(max_x):
            if matrix_data[y][x] == "^":
                start_x = x
                start_y = y
            if matrix_data[y][x] == "#":
                obstacles.add((x, y))
    
    cur_x, cur_y = start_x, start_y
    
    new_obvs = set()
    
    unique_points = set()
    turning_points = set()
    
    def is_valid(x, y):
        return 0 <= x < max_x and 0 <= y < max_y
    
    pos_mov_map = {
        "up": "right",
        "right": "down",
        "down": "left",
        "left": "up"
    }
    unique_points.add((cur_x, cur_y))
    while(is_valid(cur_x, cur_y)):
        if pos_mov == "up":
            if (cur_x, cur_y) in obstacles:
                pos_mov = pos_mov_map[pos_mov]
                cur_y += 1
                cur_x += 1
                continue
            unique_points.add((cur_x, cur_y))
            cur_y -= 1
        if pos_mov == "right":
            if (cur_x, cur_y) in obstacles:
                pos_mov = pos_mov_map[pos_mov]
                cur_x -= 1
                cur_y += 1
                continue
            unique_points.add((cur_x, cur_y))
            cur_x += 1
        if pos_mov == "down":
            if (cur_x, cur_y) in obstacles:
                pos_mov = pos_mov_map[pos_mov]
                cur_y -= 1
                cur_x -= 1
                continue
            unique_points.add((cur_x, cur_y))
            cur_y += 1
        if pos_mov == "left":
            if (cur_x, cur_y) in obstacles:
                pos_mov = pos_mov_map[pos_mov]
                cur_x += 1
                cur_y -= 1
                continue
            unique_points.add((cur_x, cur_y))
            cur_x -= 1
        
    def is_loop(obstacles, start, max_x, max_y):
        visited = set()
        x, y = start
        direction = -1j

        while 0 <= x < max_x and 0 <= y < max_y:
            if ((x, y), direction) in visited:
                return True
            visited.add(((x, y), direction))
            next_pos = (x + direction.real, y + direction.imag)
            while next_pos in obstacles:
                direction = direction * 1j
                next_pos = (x + direction.real, y + direction.imag)
            x, y = next_pos

        return False
    
    print(len(unique_points)) # part 1
    
    g_pos = set()
    unique_points.remove((start_x, start_y))
    for point in unique_points:
        obstacles.add(point)
        if is_loop(obstacles, (start_x, start_y), max_x, max_y):
            g_pos.add(point)
        obstacles.remove(point)
    print(len(g_pos)) # part 2