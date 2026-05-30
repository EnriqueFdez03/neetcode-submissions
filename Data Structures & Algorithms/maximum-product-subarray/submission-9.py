class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = nums[0], nums[0]

        for i in range(1, len(nums)):
            temp = currMax
            currMax = max(nums[i], currMax * nums[i], currMin * nums[i])
            currMin = min(nums[i], temp * nums[i], currMin * nums[i])
            res = max(res, currMax)

        return res