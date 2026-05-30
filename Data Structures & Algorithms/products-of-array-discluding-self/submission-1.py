# 1  1  2  8
# 48 24 6  1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        toRight = [1] * len(nums)
        toLeft = [1] * len(nums)
        for i in range(1, len(nums)):
            toRight[i] = toRight[i - 1] * nums[i - 1]        

        for i in range(len(nums) - 2, -1, -1):
            toLeft[i] = toLeft[i + 1] * nums[i + 1]

        return [a*b for a, b in zip(toRight, toLeft)]