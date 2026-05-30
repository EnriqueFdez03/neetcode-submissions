class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        cache = {}
        def dfs(i, j):
            if j == m:
                return 1
            if i >= n:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
        
            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            
            cache[(i, j)] = res
            return res

        return dfs(0, 0)
