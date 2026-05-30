from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        acum = defaultdict(int)

        for cs in s:
            acum[cs] += 1
        
        for ct in t:
            acum[ct] -= 1

        return all(n == 0 for n in acum.values())
        