class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2

        cache = {}
        def dfs(i, amount): # whether we pick i or not
            if amount == target and i < len(nums):
                return True
            if amount > target or i >= len(nums):
                return False
            if (i, amount) in cache:
                return cache[(i, amount)]

            cache[(i, amount)] = dfs(i + 1, amount + nums[i]) or dfs(i + 1, amount)

            return cache[(i, amount)]

        return dfs(0,0)