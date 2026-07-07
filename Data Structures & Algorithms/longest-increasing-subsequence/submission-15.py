# 9 1 4 2 3 3 7
# 1 1 2 2 3 3 4

# 0 3 1 3 2 3
# 1 2 2 3 3 4

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # let state i be dfs(i) - longest subsequence apart i
        n = len(nums)
        cache = [-1] * n

        def dfs(i):
            if i == n:
                return 0
            if cache[i] != -1:
                return cache[i]
            
            LIS = 1
            for j in range(i, n):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))
            
            cache[i] = LIS
            return LIS
        
        return max(dfs(i) for i in range(n))
        