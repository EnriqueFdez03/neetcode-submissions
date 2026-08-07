class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, currSum, path):
            if currSum == target:
                res.append(path.copy())
                return
            
            for j in range(i, len(nums)):
                if currSum + nums[j] > target:
                    return
                path.append(nums[j])
                dfs(j, currSum + nums[j], path)
                path.pop() 

        dfs(0, 0, [])
        return res