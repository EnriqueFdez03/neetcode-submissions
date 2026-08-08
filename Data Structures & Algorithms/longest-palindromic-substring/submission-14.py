class Solution:
    def longestPalindrome(self, s: str) -> str:
        # ababab  - > s[3:5] is palindrome if s[3] == s[5] and s[i+1:j-1] s[4:4] is palindrome
        cache = {}
        maxLen = 0
        bestI = -1
 
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or (i + 1, j - 1) in cache and cache[(i + 1, j - 1)]):
                    cache[(i, j)] = True
                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        bestI = i
        
        return s[bestI: bestI + maxLen]