from util.input import get_input_as_list

def check_designs(patterns, designs, total_checks=False):
    pattern_set = set(patterns)
    max_pattern_len = max(len(pattern) for pattern in patterns)
    
    def can_form_design(design):
        dp = [False] * (len(design) + 1)
        dp[0] = 1 if total_checks else True
        
        for i in range(1, len(design) + 1):
            for j in range(1, max_pattern_len + 1):
                if i >= j and design[i-j:i] in pattern_set and dp[i-j]:
                    dp[i] += dp[i-j]if total_checks else True
                    if total_checks == False:
                        break
        return dp[len(design)]
    return sum(can_form_design(design) for design in designs)
    

if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_19.txt")
    patterns = [x.replace(",", "") for x in input_data[0]]
    designs = [x[0] for x in input_data[2:]]
    print(check_designs(patterns, designs)) # Part 1
    print(check_designs(patterns, designs, True)) # Part 2