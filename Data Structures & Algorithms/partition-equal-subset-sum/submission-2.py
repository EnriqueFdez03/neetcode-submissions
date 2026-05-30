class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2

        def dfs(i, amount): # whether we pick i or not
            if amount == target and i < len(nums):
                return True
            if amount > target or i >= len(nums):
                return False
            
            if dfs(i + 1, amount + nums[i]) or dfs(i + 1, amount):
                return True
            return False

        return dfs(0,0)