class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up. dp[i]: maximum amount robbed till house i
        cache = [-1] * len(nums)
        def dfs(i): # maximum amount till house ith
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]

            cache[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return cache[i]

        return dfs(0)