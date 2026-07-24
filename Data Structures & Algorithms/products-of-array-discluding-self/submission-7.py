class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        res = [1] * len(nums)
        for i, num in enumerate(nums):
            res[i] *= pre
            pre *= num
        
        post = 1
        for i, num in enumerate(reversed(nums)):
            res[len(nums) - 1 - i] *= post
            post *= num

        return res