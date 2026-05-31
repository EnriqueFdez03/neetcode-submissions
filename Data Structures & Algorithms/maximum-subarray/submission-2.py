class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # state [i][flag]; i is in subarray; i is not i subarray
        n = len(nums)
        cache = [[-1] * 2 for _ in range(n)]

        def dfs(i, flag):
            if i == n - 1:
                return max(0, nums[i]) if flag else nums[i]
            if cache[i][flag] != -1:
                return cache[i][flag]
            
            res = None
            if flag:
                res = max(0, nums[i] + dfs(i + 1, True))
            else:
                res = max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))
            cache[i][flag] = res
            return res
        
        return dfs(0, False)
