class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cache = [[False] * n for _ in range(n)]
        count = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or cache[i+1][j-1]):
                    count += 1
                    cache[i][j] = True
        return count