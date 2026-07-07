class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # state [i][flag]; i is in subarray; i is not i subarray
        n = len(nums)
        cache = [[-1] * 2 for _ in range(len(nums))]
        def dfs(i, flag):
            if i == n:
                return float('-inf') if not flag else 0
            if cache[i][flag] != -1:
                return cache[i][flag]

            res = 0
            if flag: # we are in a subarray
                res = max(res, nums[i] + dfs(i + 1, True))
            else:
                res = max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))
            cache[i][flag] = res

            return res
    
        return dfs(0, False)
