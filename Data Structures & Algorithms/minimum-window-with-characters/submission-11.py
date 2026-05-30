from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        dictT = defaultdict(int)
        for c in t:
            dictT[c] += 1
        
        dictS = defaultdict(int)
        l = 0
        minL, maxR = 0, 0
        alreadyValidRange = False # tracks if we already got a valid window.
        for r in range(len(s)):
            dictS[s[r]] += 1

            while len(dictS) >= len(dictT) and all(c in dictS and dictS[c] >= r for c, r in dictT.items()):
                if not alreadyValidRange or maxR - minL > r - l:
                    minL, maxR = l, r
                alreadyValidRange = True
                dictS[s[l]] -= 1
                l += 1

        return s[minL:maxR+1] if alreadyValidRange else ""               