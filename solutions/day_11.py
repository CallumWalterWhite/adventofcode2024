from util.input import get_input_as_list
import concurrent.futures
from typing import List, Dict

class RecursiveSetSolver:
    def __init__(self):
        self.cache: Dict[str, List[str]] = {}
        self.cache_lock = concurrent.futures.thread.Lock()

    def recursive_set(self, num: str, b: int) -> List[str]:
        if b == 75:
            return [num]
        
        result: List[str] = []
        if num == "0":
            result = ["1"]
        elif len(num) % 2 == 0:
            mid = len(num) // 2
            left_num = int(num[:mid])
            right_num = int(num[mid:])
            result = [str(left_num), str(right_num)]
        else:
            new_num = str(int(num) * 2024)
            result = [new_num]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            recursive_results = list(executor.map(
                lambda r: self.recursive_set(r, b + 1), 
                result
            ))
        flattened_results = [
            item for sublist in recursive_results 
            for item in (sublist if isinstance(sublist, list) else [sublist])
        ]

        return flattened_results

    def solve(self, input_data: List[str]) -> int:
        final_result = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(
                lambda num: self.recursive_set(num, 0), 
                input_data
            ))
        final_result = [
            item for sublist in results 
            for item in (sublist if isinstance(sublist, list) else [sublist])
        ]

        return len(final_result)
    
if __name__ == "__main__":
    input_data = get_input_as_list("inputs/day_11.txt")[0]
    blinks = 25
    
    cache = {}
    for b in range(blinks):
        cur_data = input_data
        new_data = []  
        for num in cur_data:
            if num in cache:
                new_data.extend(cache[num])
                continue
            if num == "0":
                new_data.extend("1")
                cache[num] = ["1"]
                continue
            if len(num) % 2 == 0:
                mid = len(num) // 2
                left_num = int(num[:mid])
                right_num = int(num[mid:])
                new_data.append(str(left_num))
                new_data.append(str(right_num))
                cache[num] = [str(left_num), str(right_num)]
                continue
            new_num = str(int(num) * 2024)
            new_data.append(new_num)
            cache[num] = [new_num]
        input_data = new_data 
        print(b)
    print(len(input_data))
    solver = RecursiveSetSolver()
    result = solver.solve(list(input_data))
    print(len(result))