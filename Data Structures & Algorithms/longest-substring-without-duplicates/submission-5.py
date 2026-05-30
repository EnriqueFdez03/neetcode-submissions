class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        l, r = 0, 1

        reps = { s[l] }
        res = 1
        while r < len(s):
            while s[r] in reps:
                reps.remove(s[l])
                l += 1
            
            reps.add(s[r])
            res = max(res, r - l + 1)
            r += 1

        return res
