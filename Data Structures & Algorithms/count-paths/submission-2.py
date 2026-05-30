class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # tip: instead of trying to figuring out everything, think
        # as you are already in the solution and want to check from where you can
        # come from, this way you realise f(r, c) = f(r - 1, c) + f(r, c - 1)
        cache = [[-1] * n for _ in range(m)]
        def dfs(r, c):
            if cache[r][c] != -1:
                return cache[r][c]
            if r == 0 or c == 0:
                return 1
            if r < 0 or c < 0:
                return 0
            res = dfs(r - 1, c) + dfs(r, c - 1)
            cache[r][c] = res
            return res

        return dfs(m - 1, n - 1)