class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n
        
        def dfs(i):
            if i >= n:
                return 0
            if cache[i] != -1:
                return cache[i]

            LSI = 1
            for j in range(i, n):
                if nums[i] < nums[j]:
                    LSI = max(LSI, dfs(j) + 1)
            cache[i] = LSI
            return LSI
        
        return max(dfs(i) for i in range(n))
        