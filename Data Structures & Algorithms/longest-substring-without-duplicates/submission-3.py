# pwwekcl
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        trackedNumbers = set()
        i, j, res = 0, 0, 0
        while j < len(s):
            while s[j] in trackedNumbers:
                trackedNumbers.remove(s[i])
                i += 1
            
            trackedNumbers.add(s[j])
            res = max(res, j - i + 1)

            j += 1    

        return res