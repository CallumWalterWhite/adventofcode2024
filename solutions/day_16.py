import heapq
from util.input import get_input_as_list

def get_neighbors(x, y):
    directions = {
        ">": (1, 0),
        "<": (-1, 0),
        "^": (0, -1),
        "v": (0, 1)
    }
    for new_dir, (dx, dy) in directions.items():
        yield x + dx, y + dy, new_dir
        
if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_16.txt")
    maze = [row[0] for row in input_data]
    start_x, start_y, end_x, end_y = 0, 0, 0, 0
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "S":
                start_x, start_y = x, y
            if maze[y][x] == "E":
                end_x, end_y = x, y
    queue = []
    heapq.heappush(queue, (0, start_x, start_y, ">", 0))
    visited = set()
    while queue:
        cost, x, y, direction, turns = heapq.heappop(queue)
        if (x, y) == (end_x, end_y):
            print(cost)
            break
        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        for nx, ny, new_dir in get_neighbors(x, y):
            if maze[ny][nx] == "#":
                continue
            new_turns = turns + (1 if new_dir != direction else 0)
            new_cost = cost + 1 + (1000 if new_dir != direction else 0)
            heapq.heappush(queue, (new_cost, nx, ny, new_dir, new_turns))
