from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        chars = defaultdict(int)
        maxLen = 0
        
        while r < len(s):
            while l < r and self.getReplacements(chars) > k:
                chars[s[l]] -= 1
                l += 1
            
            chars[s[r]] += 1
            if self.getReplacements(chars) <= k:       
                maxLen = max(maxLen, r - l + 1)
            r += 1    
            print(chars)

        return maxLen

    def getReplacements(self, chars: dict):
        mostRep = 0
        totals = 0
        for r in chars.values():
            totals += r
            mostRep = max(r, mostRep)
        
        return totals - mostRep



