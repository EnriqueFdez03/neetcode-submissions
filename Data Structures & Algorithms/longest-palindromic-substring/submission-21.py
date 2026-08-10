class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        cache = [[False] * n for _ in range(n)]
        maxLen = 0
        bestI = None

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or cache[i + 1][j - 1]):
                    cache[i][j] = True
                    if j - i + 1 >= maxLen:
                        maxLen = j - i + 1
                        bestI = i
        
        return s[bestI:bestI + maxLen]
