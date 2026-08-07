class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()

        def dfs(i, path):
            if i >= len(nums):
                return
            
            path.append(nums[i])
            res.append(path.copy())
            dfs(i + 1, path)
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            path.pop()
            dfs(i + 1, path)
        
        dfs(0, [])
        return res