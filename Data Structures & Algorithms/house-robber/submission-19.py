class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            
            amount = max(nums[i] + dfs(i + 2), dfs(i + 1))
            cache[i] = amount
            return amount

        return dfs(0)