from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1Reps = defaultdict(int)
        for c in s1:
            s1Reps[c] += 1

        windowCount = defaultdict(int)
        l, r = 0, 0
        while r < len(s2):
            windowCount[s2[r]] += 1
            if r - l + 1 == len(s1):
                if s1Reps == windowCount:
                    return True
                else:
                    windowCount[s2[l]] -= 1
                    if windowCount[s2[l]] == 0:
                        del windowCount[s2[l]]
                    l += 1

            r += 1

        return False
