from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxLen = 0
        repsDict = defaultdict(int)

        while r < len(s):
            repsDict[s[r]] += 1
            while self.currK(repsDict) > k:
                repsDict[s[l]] -= 1
                l += 1
            
            print(repsDict)
            print(self.currK(repsDict))

            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen

    def currK(self, repsDict) -> int:
        maxReps = 0
        res = 0
        for reps in repsDict.values():
            maxReps = max(maxReps, reps)
            res += reps

        return res - maxReps