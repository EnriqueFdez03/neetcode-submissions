from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictS = defaultdict(int)
        dictT = defaultdict(int)
        length = len(s)

        for i in range(length):
            dictS[s[i]] += 1
            dictT[t[i]] += 1
        
        return dictS == dictT
