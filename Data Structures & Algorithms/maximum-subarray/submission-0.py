class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        maxSum = nums[0]
        for i in range(n):
            currSum = 0
            for j in range(i, -1, -1):
                currSum += nums[j]
                maxSum = max(maxSum, currSum)
        return maxSum