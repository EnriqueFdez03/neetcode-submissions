class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        l, r = 0, 0
        chars = set()
        maxLen = 0
        while r < len(s):
            while s[r] in chars and l < r:
                chars.remove(s[l])
                l += 1
            
            chars.add(s[r])
            maxLen = max(maxLen, r - l + 1)
            r += 1

        return maxLen

