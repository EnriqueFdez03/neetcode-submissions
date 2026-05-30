from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = defaultdict(int)
        for c in t:
            tDict[c] += 1
        
        windowDict = defaultdict(int)
        candidateR = None
        candidateL = None
        candidateLen = None
        l = 0
        for r in range(len(s)):

            windowDict[s[r]] += 1
            while len(windowDict) >= len(tDict) and self.windowSatisfies(tDict, windowDict):
                if not candidateLen or candidateLen > (r - l) + 1:
                    candidateLen = (r - l) + 1
                    candidateR, candidateL = r, l  

                windowDict[s[l]] -= 1
                if windowDict[s[l]] == 0:
                    del windowDict[s[l]]
                l += 1                

        if candidateL == None:
            return ""

        return s[candidateL:candidateR+1]

        
    def windowSatisfies(self, tDict, windowDict):
        for c, rep in tDict.items():
            if c not in windowDict or windowDict[c] < rep:
                return False
        return True