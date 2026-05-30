class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up. dp[i]: maximum amount robbed till house i
        dp = [n for n in nums]

        for i in range(len(nums)):
            if i >= 2:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            elif i == 1:
                dp[i] = max(dp[i - 1], dp[i])
         
        print(dp)
        return max(dp)
