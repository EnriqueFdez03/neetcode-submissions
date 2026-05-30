class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # state [i][flag]; i is in subarray; i is not i subarray
        cache = [[None] * 2 for _ in range(len(nums))]
        def dfs(i, flag):
            if cache[i][flag] is not None:
                return cache[i][flag]
            if i == len(nums) - 1:
                return max(0, nums[i]) if flag else nums[i]

            if flag:
                cache[i][flag] = max(0, nums[i] + dfs(i + 1, True))
                return cache[i][flag]
            else:
                cache[i][flag] = max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))
                return cache[i][flag]
        return dfs(0, False)