class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def backtrack(i, path): # choose if i is included in path
            if i >= len(nums):
                return
            
            path.append(nums[i])
            res.append(path.copy())
            backtrack(i + 1, path)
            path.pop()
            backtrack(i + 1, path)

        backtrack(0, [])
        return res
