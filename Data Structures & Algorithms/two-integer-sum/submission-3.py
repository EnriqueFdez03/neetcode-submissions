class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aux = dict()

        for idx, num in enumerate(nums):
            if num in aux:
                return [aux[num], idx]
            
            aux[target - num] = idx
        
        