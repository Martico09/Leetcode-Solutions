class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, val1 in enumerate(nums):
            
            for j, val2 in enumerate(nums):
                
                if (val1+val2) == target and i!=j:
                    return [i, j]