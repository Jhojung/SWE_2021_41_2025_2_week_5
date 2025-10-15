from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_map = {}
    
    for i, n in enumerate(nums):
        complement = target - n
        
        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[n] = i