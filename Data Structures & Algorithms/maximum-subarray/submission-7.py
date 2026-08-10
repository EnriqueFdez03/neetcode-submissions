class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [[None] * 2 for _ in range(n)]

        def dfs(i, picking):
            if i == n:
                return 0 if picking else float('-inf')
            if cache[i][picking] != None:
                return cache[i][picking]
            
            res = 0
            if picking:
                res = max(nums[i] + dfs(i + 1, True), 0)
            else:
                res = max(nums[i] + dfs(i + 1, True), dfs(i + 1, False))
            
            cache[i][picking] = res
            return res
        
        return dfs(0, False)
