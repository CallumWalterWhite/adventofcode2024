import heapq
from util.input import get_input_as_list
from itertools import product

def find_all_paths(pad, start_x, start_y, target):
    queue = []
    heapq.heappush(queue, (0, start_x, start_y, "", set()))
    paths = []
    while queue:
        cost, x, y, path, visted = heapq.heappop(queue)
        if pad[y][x] == target:
            paths.append((path, cost, y, x))
            continue
        if (x, y) in visted:
            continue
        
        visted.add((x, y))
        directions = {
            "^": (0, -1),
            "v": (0, 1),
            "<": (-1, 0),
            ">": (1, 0)
        }
        
        for direction in directions.keys():
            dx, dy = directions[direction]
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= len(pad[0]) or ny >= len(pad):
                continue
            if pad[ny][nx] is None:
                continue
            new_cost = cost + 1
            heapq.heappush(queue, (new_cost, nx, ny, path + direction, visted))
            
    return paths


def find_directional_path(pad, start_x, start_y, target):
    queue = []
    heapq.heappush(queue, (0, start_x, start_y, ""))
    # visited = set()
    while queue:
        cost, x, y, path = heapq.heappop(queue)
        if pad[y][x] == target:
            return (path, x, y)
            break
        # if (x, y) in visited:
        #     continue
        # visited.add((x, y))

        directions = {
            "^": (0, -1),
            "v": (0, 1),
            "<": (-1, 0),
            ">": (1, 0)
        }
        
        prev_direction = path[-1] if path else None
        for direction in directions.keys():
            dx, dy = directions[direction]
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= len(pad[0]) or ny >= len(pad):
                continue
            if pad[ny][nx] is None:
                continue
            new_cost = cost + 1
            if prev_direction != direction and prev_direction is not None:
                new_cost += 1
            heapq.heappush(queue, (new_cost, nx, ny, path + direction))
            
    return None

    

if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_21.txt")
    codes = [line[0] for line in input_data]
    numeric_pad = [[7,8,9],[4,5,6],[1,2,3], [None, 0, 'A']]
    directional_pad = [[None, '^', 'A'], ['<', 'v', '>']]
    
    code_paths = []
    for code in codes:
        start_x, start_y = 2, 3
        full_code = ""
        for num in code:
            if num != 'A':
                num = int(num)
            path, start_x, start_y = find_directional_path(numeric_pad, start_x, start_y, num)
            full_code += path + 'A'
        code_paths.append(full_code)
    
    more_code_paths = []
    for code_path in code_paths:
        start_x, start_y = 2, 0
        full_code = ""
        for direction in code_path:
            path, start_x, start_y = find_directional_path(directional_pad, start_x, start_y, direction)
            full_code += path + 'A'
        more_code_paths.append(full_code)
    path_lengths = []
    for code in more_code_paths:
        start_x, start_y = 2, 0
        full_code = ""
        for direction in code:
            path, start_x, start_y = find_directional_path(directional_pad, start_x, start_y, direction)
            full_code += path + 'A'
        path_lengths.append(len(full_code))
    total = 0
    for i in range(len(codes)):
        total += int(codes[i].replace("([^0].*)", "").replace("A", "")) * path_lengths[i]
    print(total) # Part 1
    
    code_paths = {}
    
    for code in codes:
        start_x, start_y = 2, 3
        for num in code:
            if num != 'A':
                num = int(num)
            paths = find_all_paths(numeric_pad, start_x, start_y, num)
            for path, cost, y, x in paths:
                start_x, start_y = x, y
                path += "A"
                if code not in code_paths:
                    code_paths[code] = {}
                if num not in code_paths[code]:
                    code_paths[code][num] = []
                code_paths[code][num].append(path)
    new_code_paths = {}
    for code in code_paths:
        all_combinations = list(
            product(
                *[code_paths[code][key] for key in code_paths[code]]
            )
        )
        new_code_paths[code] = []
        for combo in all_combinations:
            new_code = "".join(combo)
            new_code_paths[code].append(new_code)
            
    code_paths = {}
    for code in new_code_paths:
        start_x, start_y = 2, 0
        for cpath in new_code_paths[code]:
            for num in cpath:
                paths = find_all_paths(directional_pad, start_x, start_y, num)
                for path, cost, y, x in paths:
                    start_x, start_y = x, y
                    path += "A"
                    if code not in code_paths:
                        code_paths[code] = {}
                    if num not in code_paths[code]:
                        code_paths[code][num] = []
                    code_paths[code][num].append(path)
                    
    new_code_paths = {}
    for code in code_paths:
        all_combinations = list(
            product(
                *[code_paths[code][key] for key in code_paths[code]]
            )
        )
        new_code_paths[code] = []
        for combo in all_combinations:
            new_code = "".join(combo)
            new_code_paths[code].append(new_code)
                
    print(new_code_paths)
    # print(code_paths)