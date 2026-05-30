class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()

        def backtrack(i, path):
            if i >= len(nums):
                return
            
            path.append(nums[i])
            res.append(path.copy())
            backtrack(i + 1, path)
            path.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, path)

        backtrack(0, [])
        return res