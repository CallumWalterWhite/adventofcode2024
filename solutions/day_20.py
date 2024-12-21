import heapq
from util.input import get_input_as_list

def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end="")
        print()

def steps_to_exit(grid, start_x, start_y, end_x, end_y):
    queue = []
    heapq.heappush(queue, (0, start_x, start_y, [(start_x, start_y)]))
    visited = set()
    while queue:
        cost, x, y, path = heapq.heappop(queue)
        if (x, y) == (end_x, end_y):
            return (cost, path)
            break
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for nx, ny, dir in [(x+1, y, "r"), (x-1, y, "l"), (x, y+1, "u"), (x, y-1, "d")]:
            if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
                continue
            if grid[ny][nx] == "#":
                continue
            heapq.heappush(queue, (cost + 1, nx, ny, path + [(nx, ny)]))
    return (None, None)

if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_20.txt")
    grid = [x[0] for x in input_data]
    start_x, start_y, end_x, end_y = 0, 0, 0, 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                start_x, start_y = x, y
            if grid[y][x] == "E":
                end_x, end_y = x, y
    (steps, path) = steps_to_exit(grid, start_x, start_y, end_x, end_y)
    min_saving = 100
    no_cheat = 0
    cheats = [[2,0],[0,2],[-2,0],[0,-2],[1,1],[1,-1],[-1,1],[-1,-1]]
    checked = set()
    for idx, pos in enumerate(path):
        for cheat in cheats:
            if (pos[0]+cheat[0],pos[1]+cheat[1]) in path[:idx]:
                saving = idx - 2 - path.index((pos[0]+cheat[0],pos[1]+cheat[1]))
                if saving >= min_saving:
                    no_cheat += 1
    print(no_cheat)
    max_cheat = 20
    no_cheat = 0
    for idx, pos in enumerate(path):
        if len(path)-1-idx < min_saving:
            break
        for idx_2, pos_2 in enumerate(path[(idx+min_saving):]):
            distance = abs(pos[0]-pos_2[0]) + abs(pos[1]-pos_2[1])
            if distance <= max_cheat:
                saving = path.index((pos_2[0],pos_2[1])) - distance - path.index((pos[0],pos[1]))
                if saving >= min_saving:
                    no_cheat += 1
    print(no_cheat)