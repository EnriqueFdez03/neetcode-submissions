class Solution:
    def longestPalindrome(self, s: str) -> str:
        cache = {}
        maxLen = 0
        bestI = -1

        for i in range(len(s) - 1, -1, -1): # the pair (i, j) is palindrome
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or (i + 1, j - 1) in cache and cache[(i + 1, j - 1)]):
                    cache[(i, j)] = True
                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        bestI = i
        
        return s[bestI: bestI + maxLen]