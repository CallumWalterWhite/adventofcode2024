import math
from util.input import get_input_as_list
    
if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_12.txt")
    grid = [x[0] for x in input_data]
    join_regions = []
    visited = set()
    def dfs_cord_join(x, y, char):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != char:
            return []
        if (x, y) in visited:
            return []
        result = [(x, y)]
        visited.add((x, y))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            result.extend(dfs_cord_join(x + dx, y + dy, char))
        return result
    
    def calculate_perimeter(region, v):
        stack = region.copy()
        visited = set()
        perimeter = 0
        while len(stack) != 0:
            x, y = stack.pop()
            visited.add((x, y))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                if x + dx < 0 or x + dx >= len(grid) or y + dy < 0 or y + dy >= len(grid[0]):
                    perimeter += 1
                    continue
                if grid[x + dx][y + dy] != v:
                    perimeter += 1
                    continue
        return perimeter
    
    def calculate_total_sides(region):
        up_sides = 0
        down_sides = 0
        left_sides = 0
        right_sides = 0
        for (x, y) in region:
            left = x - 1
            right = x + 1
            above = y - 1
            below = y + 1
            right_not_in_region = (right, y) not in region
            below_not_region = (x, below) not in region
            if (x, above) not in region:
                if right_not_in_region or (right, above) in region:
                    up_sides += 1
            if (x, below) not in region:
                if right_not_in_region or (right, below) in region:
                    down_sides += 1
            if (left, y) not in region:
                if below_not_region or (left, below) in region:
                    left_sides += 1
            if (right, y) not in region:
                if below_not_region or (right, below) in region:
                    right_sides += 1
        return up_sides + down_sides + left_sides + right_sides
    
    total_perimeter_price = 0
    total_area_price = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in visited:
                continue
            region = dfs_cord_join(i, j, grid[i][j])
            join_regions.append(region)
            perimeter = calculate_perimeter(region, grid[i][j])
            sides = calculate_total_sides(region)
            total_perimeter_price += len(region) * perimeter
            total_area_price += len(region) * sides
    print(total_perimeter_price) # part 1
    print(total_area_price) # part 2