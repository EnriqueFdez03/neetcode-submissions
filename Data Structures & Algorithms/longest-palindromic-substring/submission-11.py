class Solution:
    def longestPalindrome(self, s: str) -> str:
        # ababbaba
        maxLen = 0
        res = ""
        n = len(s)

        cache = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and(j - i <= 2 or cache[i+1][j-1]):
                    cache[i][j] = True
                    if maxLen < (j - i + 1):
                        maxLen = j - i + 1
                        res = s[i:j + 1]
            
        return res