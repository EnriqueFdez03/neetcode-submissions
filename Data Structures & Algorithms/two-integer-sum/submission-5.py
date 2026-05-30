class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        acum = {}

        for i, n in enumerate(nums):
            if n in acum:
                return [acum[n], i]        
            acum[target - n] = i