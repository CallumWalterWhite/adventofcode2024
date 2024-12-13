from util.input import get_input_as_list

if __name__ == '__main__':
    input_data = get_input_as_list("inputs/day_8.txt")
    grid = [row[0] for row in input_data]
    antennas = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    
    antinodes = set()
    grid_width = len(grid[0])
    grid_height = len(grid)
                
    for freq, locations in antennas.items():
        for i in range(len(locations)):
            for j in range(i+1, len(locations)):
                x1, y1 = locations[i]
                x2, y2 = locations[j]
                
                dx = x2 - x1
                dy = y2 - y1
                
                antinode1_x = x1 - dx
                antinode1_y = y1 - dy
                
                antinode2_x = x2 + dx
                antinode2_y = y2 + dy
                
                grid_width = len(grid[0])
                grid_height = len(grid)
                
                if (0 <= antinode1_x < grid_width and 
                    0 <= antinode1_y < grid_height):
                    antinodes.add((antinode1_x, antinode1_y))
                
                if (0 <= antinode2_x < grid_width and 
                    0 <= antinode2_y < grid_height):
                    antinodes.add((antinode2_x, antinode2_y))
    
    print(len(antinodes)) # Part 1