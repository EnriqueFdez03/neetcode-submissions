class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preMults = []
        res = [1] * len(nums)

        pre = 1
        for num in nums:
            preMults.append(pre)
            pre *= num

        post = 1
        for i, num in enumerate(reversed(nums)):
            res[len(nums) - i - 1] *= post * preMults[len(nums) - i - 1]
            post *= num

        return res