class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictS = defaultdict(int)
        dictT = defaultdict(int)

        for i in range(len(s)):
            dictS[s[i]] += 1
            dictT[t[i]] += 1
        
        equal = True
        for charS, occur1 in dictS.items():
            if dictT.get(charS, 0) != occur1:
                return False

        return True
