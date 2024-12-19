import heapq
from util.input import get_input_as_list

def steps_to_exit(grid, start_x, start_y, end_x, end_y):
    queue = []
    heapq.heappush(queue, (0, start_x, start_y))
    visited = set()
    while queue:
        cost, x, y = heapq.heappop(queue)
        if (x, y) == (end_x, end_y):
            return cost
            break
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
                continue
            if grid[ny][nx] == 1:
                continue
            heapq.heappush(queue, (cost + 1, nx, ny))
    return None

if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_18.txt")
    grid_size = (70,70)
    falling_bytes_cords = [line[0].split(",") for line in input_data]
    grid = [[0 for _ in range(grid_size[0] + 1)] for _ in range(grid_size[1] + 1)]
    for x, y in falling_bytes_cords[:1024]:
        x = int(x)
        y = int(y)
        grid[y][x] = 1
    print(steps_to_exit(grid, 0, 0, 70, 70)) # Part 1
    
    # Part 2 - simulate no escape (brute force)
    for checks in range(1024, len(falling_bytes_cords)):
        grid = [[0 for _ in range(grid_size[0] + 1)] for _ in range(grid_size[1] + 1)]
        for x, y in falling_bytes_cords[:checks]:
            x = int(x)
            y = int(y)
            grid[y][x] = 1
        if steps_to_exit(grid, 0, 0, 70, 70) is None:
            print(checks)
            print(falling_bytes_cords[:checks][-1])
            break