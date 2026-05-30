class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def dfs(i, cur): # nº ways to reach target from nums[i:] and cur
            if i == n and cur == target:
                return 1
            if i >= n:
                return 0
            
            return dfs(i + 1, cur + nums[i]) + dfs(i + 1, cur - nums[i])
        
        return dfs(0, 0)