class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # state - i largest subsecuence for nums[i:]
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            dp[i] = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)