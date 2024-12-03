from util.input import get_input_as_list

def check_safe(r):
    p_l = None
    inc = None
    safe = True
    for l in r:
        l = int(l)
        if p_l is None:
            p_l = l
            continue
        if p_l == l:
            safe = False
            break
        if inc is None:
            if l > p_l:
                inc = True
            else:
                inc = False
        if abs(l - p_l) > 3:
            safe = False
            break
        if inc == True and l < p_l:
            safe = False
            break
        if inc == False and l > p_l:
            safe = False
            break
        p_l = l
    return safe

def part_1(input_data):
    total_safe = 0
    for r in input_data:
        safe = check_safe(r)
        if safe:
            total_safe += 1 
    return total_safe

def part_2(input_data):
    total_safe = 0
    for r in input_data:
        c_safe = check_safe(r)
        if c_safe == True:
            total_safe += 1 
            continue
        for i in range(len(r)):
            test_report = r[:i] + r[i+1:]
            if check_safe(test_report):
                total_safe += 1
                break
    return total_safe

if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_2.txt")
    print(part_1(input_data))
    print(part_2(input_data))