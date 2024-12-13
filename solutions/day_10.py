from util.input import get_input_as_list

if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_10.txt")
    topo_map = [x[0] for x in input_data]
    max_x = len(topo_map[0])
    max_y = len(topo_map)
    
    def dfs_trailhead(x, y, n_v):
        if x < 0 or x >= max_x or y < 0 or y >= max_y:
            return []
        if int(topo_map[y][x]) != n_v:
            return []
        if int(topo_map[y][x]) == 9:
            return [(x, y)]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        result = []
        for d in directions:
            result.extend(dfs_trailhead(x + d[0], y + d[1], n_v + 1))
        return result
    
    def dfs_trailhead_dis(x, y, n_v):
        if x < 0 or x >= max_x or y < 0 or y >= max_y:
            return 0
        if int(topo_map[y][x]) != n_v:
            return 0
        if int(topo_map[y][x]) == 9:
            return 1
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        results = 0
        for d in directions:
            results += dfs_trailhead_dis(x + d[0], y + d[1], n_v + 1)
        return results
    
    trails = []
    for i in range(max_y):
        for j in range(max_x):
            if topo_map[i][j] == "0":
                trails.append({
                    "start": (j, i),
                    "trail": set(dfs_trailhead(j, i, 0)),
                    "distinct": dfs_trailhead_dis(j, i, 0)
                })
    print(sum([len(trail["trail"]) for trail in trails])) # part 1
    print(sum([trail["distinct"] for trail in trails])) # part 2
