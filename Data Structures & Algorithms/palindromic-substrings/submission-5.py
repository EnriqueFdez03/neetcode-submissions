class Solution:
    def countSubstrings(self, s: str) -> int:
        cache = {}
        res = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or (i + 1, j - 1) in cache and cache[(i + 1, j - 1)]):
                    cache[(i, j)] = True
                    res += 1
        
        return res