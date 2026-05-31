class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        cache = [[-1] * m for _ in range(n)]
        def dfs(i, j):
            if j == m: # I consumed word2, so I need to remove n - i
                return n - i
            if i == n: # I consumed word1, so I need to insert m - j
                return m - j
            if cache[i][j] != -1:
                return cache[i][j]
            
            if word1[i] == word2[j]:
                cache[i][j] = dfs(i + 1, j + 1)
            else:
                # replace i + 1, j + 1
                # remove i + 1, j
                # insert i, j + 1
                cache[i][j] = 1 + min(dfs(i + 1, j + 1), dfs(i + 1, j), dfs(i, j + 1))
            return cache[i][j]

        return dfs(0, 0)