class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, currSum, path):
            if currSum == target:
                res.append(path.copy())
                return
            if i >= len(nums) or currSum > target:
                return

            path.append(nums[i])
            dfs(i, currSum + nums[i], path)
            path.pop()
            dfs(i + 1, currSum, path)

        dfs(0, 0, [])
        return res