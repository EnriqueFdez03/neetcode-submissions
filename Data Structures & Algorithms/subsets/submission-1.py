class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(i, path):
            if i == n:
                res.append(path[:])
                return
            
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
            dfs(i + 1, path)

        dfs(0, [])
        return res
