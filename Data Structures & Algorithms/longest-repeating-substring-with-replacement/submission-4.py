from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        repsDict = defaultdict(int)

        l = 0   
        for r in range(len(s)):
            repsDict[s[r]] += 1
            while self.currK(repsDict) > k:
                repsDict[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen

    def currK(self, repsDict) -> int:
        maxReps = 0
        res = 0
        for reps in repsDict.values():
            maxReps = max(maxReps, reps)
            res += reps

        return res - maxReps