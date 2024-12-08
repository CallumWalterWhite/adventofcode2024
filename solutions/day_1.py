from util.input import get_input_as_list

if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_1.txt")
    left_list = []
    right_list = []
    for pair in input_data:
        left_list.append(int(pair[0]))
        right_list.append(int(pair[1]))
    left_list.sort()
    right_list.sort()
    calc_similarity = {}
    total_similarity = 0
    for left in left_list:
        if left in calc_similarity:
            total_similarity += calc_similarity[left]
            break    
        similarity = 0
        for right in right_list:
            if left == right:
                similarity += 1
        calc_similarity[left] = similarity * left
        total_similarity += calc_similarity[left]
    print(sum(abs(left - right) for left, right in zip(left_list, right_list)))
    print(total_similarity)