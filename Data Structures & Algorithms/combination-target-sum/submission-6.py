class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, path, curr):
            if curr == target:
                res.append(path.copy())
                return

            if i >= len(nums) or curr > target:
                return
            
            path.append(nums[i])
            dfs(i, path, curr + nums[i])
            path.pop()
            dfs(i + 1, path, curr)
        
        dfs(0, [], 0)
        return res