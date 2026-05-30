class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax, currMin = 1, 1

        for num in nums:
            oldCurrMax = currMax
            currMax = max(num, currMax * num, currMin * num)
            currMin = min(num, currMin * num, oldCurrMax * num)
            res = max(res, currMax)
        return res