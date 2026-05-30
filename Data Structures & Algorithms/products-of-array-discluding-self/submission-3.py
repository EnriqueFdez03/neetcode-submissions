class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre = 1
        for i, num in enumerate(nums):
            res[i] *= pre
            pre *= num

        post = 1
        for i, num in enumerate(reversed(nums)):
            res[len(nums) - i - 1] *= post
            post *= num

        return res