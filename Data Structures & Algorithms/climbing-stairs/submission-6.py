class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1)
        
        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        print(dp)
        return dp[0]
        # 1 2 3 4 5
        # 1 1 1 1 1 0
        # 5 3 2 1 1 0
