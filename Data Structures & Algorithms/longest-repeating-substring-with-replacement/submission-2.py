from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        replacements = defaultdict(int)
        for r in range(len(s)):
            while self.currK(replacements) > k:
                replacements[s[l]] -= 1
                l += 1
            
            replacements[s[r]] += 1
            if self.currK(replacements) <= k:
                res = max(res, r - l + 1)
        
        return res

    def currK(self, replacements: dict[str, int]) -> int:
        mostRep = 0
        totals = 0
        for r in replacements.values():
            totals += r
            mostRep = max(r, mostRep)
        return totals - mostRep
