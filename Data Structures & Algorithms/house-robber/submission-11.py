class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up. dp[i]: maximum amount robbed till house i
        dp = [n for n in nums]
        
        for i in range(1, len(nums)):
            if i >= 2:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            else:
                dp[i] = max(dp[i], dp[i - 1])

        return dp[len(nums) - 1]