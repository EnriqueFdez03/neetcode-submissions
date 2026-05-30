class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        acum = 1
        for i in range(1, len(nums)):
            acum *= nums[i-1]
            res[i] *= acum

        acum = 1
        for i in range(len(nums) - 2, -1, -1):
            acum *= nums[i+1]
            res[i] *= acum

        return res
