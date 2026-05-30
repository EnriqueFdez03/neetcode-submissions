class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = dict()

        for i, n in enumerate(nums):
            if n in remainders:
                return [remainders[n], i]
            remainders[target - n] = i 
