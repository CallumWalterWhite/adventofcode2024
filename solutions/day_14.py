from util.input import get_input_as_list

def parse_input(input_data):
    robots = []
    for line in input_data:
        pos_str = line[0][2:len(line[0])].split(",")
        pos_x = int(pos_str[0])
        pos_y = int(pos_str[1])
        vol_str = line[1][2:len(line[1])].split(",")
        vol_x = int(vol_str[0])
        vol_y = int(vol_str[1])
        robots.append((pos_x, pos_y, vol_x, vol_y))
    return robots

def check_easter_egg(robot_pos):
    def check(x, y, l):
        if l == 10:
            return True
        if l > 2:
            print(l)
        if (x, y) in robot_pos:
            return check(x + 1, y, l + 1)
        else:
            return False
    for pos in robot_pos:
        if check(pos[0], pos[1], 0):
            return True
    return False
            

if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_14.txt")
    robots_pos_vol = parse_input(input_data)
    max_x = 101
    max_y = 103
    max_x_h = max_x // 2
    max_y_h = max_y // 2
    robot_pos = [(x[0], x[1]) for x in robots_pos_vol]
    interations = 100000 # 100 for part 1
    for i in range(interations):
        for x in range(len(robots_pos_vol)):
            robot_pos_x = robot_pos[x][0]
            robot_pos_y = robot_pos[x][1]
            robot_vol_x = robots_pos_vol[x][2]
            robot_vol_y = robots_pos_vol[x][3]
            
            new_pos_x = robot_pos_x + robot_vol_x
            new_pos_y = robot_pos_y + robot_vol_y
            if new_pos_x >= max_x:
                new_pos_x = (new_pos_x - max_x)
            if new_pos_x < 0:
                new_pos_x = (new_pos_x + max_x)
            if new_pos_y >= max_y:
                new_pos_y = (new_pos_y - max_y)
            if new_pos_y < 0:
                new_pos_y = (new_pos_y + max_y)
            robot_pos[x] = (new_pos_x, new_pos_y)
        if check_easter_egg(robot_pos):
            print(i)
            break
        # else:
        #     print(i)
    quadrents = {}
    quadrents["tl"] = [
        0,
        max_x_h,
        0,
        max_y_h
    ]
    
    quadrents["tr"] = [
        (max_x_h) + 1,
        max_x,
        0,
        max_y_h
    ]
    
    quadrents["bl"] = [
        0,
        max_x_h,
        (max_y_h) + 1,
        max_y
    ]
    
    quadrents["br"] = [
        (max_x_h) + 1,
        max_x,
        (max_y_h) + 1,
        max_y
    ]
    quadrent_points = {}
    for quadrent in quadrents:
        quadrent_points[quadrent] = []
        for point in robot_pos:
            min_x = quadrents[quadrent][0]
            max_x = quadrents[quadrent][1]
            min_y = quadrents[quadrent][2]
            max_y = quadrents[quadrent][3]
            if min_x <= point[0] < max_x and min_y <= point[1] < max_y:
                quadrent_points[quadrent].append(point)
    sf = len(quadrent_points["tl"]) * len(quadrent_points["tr"]) * len(quadrent_points["bl"]) * len(quadrent_points["br"])
    print(sf) # part 1