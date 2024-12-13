import math
from util.input import get_input_as_list    

def parse_input(input_data, add_higher=False):
    games = []
    cur_game = {}
    for row in input_data:
        if len(row) == 0:
            continue
        if row[0] == "Button":
            cur_game[row[1].replace(":", "")] = (int(row[2].replace("X+", "").replace(",", "")), int(row[3].replace("Y+", "")))
        else:
            cur_game["prize"] = (int(row[1].replace("X=", "").replace(",", "")), int(row[2].replace("Y=", "")))
            games.append(cur_game)
            cur_game = {}
    return games

if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_13.txt")
    games = parse_input(input_data)
    max_times = 100
    prize_solutions = []
    higher_prize_solutions = []
    for game in games:
        AX = game['A'][0]
        BX = game['B'][0]
        prizeX = game['prize'][0]
        higherPriceX = game['prize'][0] + 10000000000000
        AY = game['A'][1]
        BY = game['B'][1]
        prizeY = game['prize'][1]
        higherPriceY = game['prize'][1] + 10000000000000
        xGCD = math.gcd(AX, BX)
        yGCD = math.gcd(AY, BY)
        if (prizeX % xGCD != 0):
            continue
        if (prizeY % yGCD != 0):
            continue
        
        prize_sol = None
        for i in range(0, max_times):
            for j in range(0, max_times):
                if (i * AX + j * BX == prizeX and i * AY + j * BY == prizeY):
                    prize_solutions.append((i, j))
                    prize_sol = (i, j)
                    break
    print(prize_solutions)
    print(higher_prize_solutions)
    total_prize = sum([sol[0] * 3 + sol[1] for sol in prize_solutions])
    print(total_prize) # part 1
    