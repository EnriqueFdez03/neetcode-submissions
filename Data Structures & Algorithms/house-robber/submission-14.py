class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i, amount): # decide if we rob house i
            if i >= len(nums):
                return amount
            
            if (i, amount) in cache:
                return cache[(i, amount)]

            cache[(i, amount)] = max(dfs(i + 1, amount), dfs(i + 2, amount + nums[i]))
            return cache[(i, amount)]
        
        return dfs(0, 0)