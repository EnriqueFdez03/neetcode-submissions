class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = [-1] * len(nums) 
        def dfs(i):
            if i >= len(nums) - 1:
                return True
            if cache[i] != -1:
                return cache[i]
            if nums[i] == 0:
                return False
            
            canReach = False
            for jump in range(nums[i], 0, -1):
                if dfs(i + jump):
                    canReach = True
                    break
            cache[i] = canReach
            return cache[i]
        
        return dfs(0)