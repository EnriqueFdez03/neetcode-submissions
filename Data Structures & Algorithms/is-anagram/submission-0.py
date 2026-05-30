class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictS = dict()
        dictT = dict()

        for i in range(len(s)):
            if s[i] not in dictS:
                dictS[s[i]] = 1
            else:
                dictS[s[i]] += 1

            if t[i] not in dictT:
                dictT[t[i]] = 1
            else: 
                dictT[t[i]] += 1
        
        equal = True
        for c in s:
            if c not in dictT:
                return False

            equal = equal and (dictS[c] == dictT[c])

            if not equal:
                return False
        
        return True
