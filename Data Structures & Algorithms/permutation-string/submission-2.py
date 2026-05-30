from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Reps = Counter(s1)
        wReps = defaultdict(int)
        size = len(s1)
        l = 0
        for r in range(len(s2)):
            if r - l + 1 > size:
                wReps[s2[l]] -= 1
                if wReps[s2[l]] == 0:
                    del wReps[s2[l]]
                l += 1
            
            wReps[s2[r]] += 1
            if s1Reps == wReps:
                return True
            
        return False


            


            

