class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)

        if len(s3) != n + m:
            return False
        
        cache = [[-1] * (m + 1) for _ in range(n + 1)]
        def dfs(i, j):
            if i == n and j == m:
                return True
            if cache[i][j] != -1:
                return cache[i][j]

            k = i + j

            res = False
            if i < n and s1[i] == s3[k]:
                res = res or dfs(i + 1, j)
            if j < m and s2[j] == s3[k]:
                res = res or dfs(i, j + 1)
            cache[i][j] = res

            return res

        return dfs(0, 0)
