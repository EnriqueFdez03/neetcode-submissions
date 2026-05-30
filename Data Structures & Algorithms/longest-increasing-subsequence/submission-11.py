class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # let dp[i] longest subsequence till i
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        
        for i in range(1, n):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)