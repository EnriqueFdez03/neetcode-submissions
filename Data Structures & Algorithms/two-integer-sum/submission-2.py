class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        acum = dict()

        for idx, num in enumerate(nums):
            if num in acum:
                return [acum[num], idx]
            
            acum[target-num] = idx

