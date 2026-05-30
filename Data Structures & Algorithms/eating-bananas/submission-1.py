from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # actually these ones aren't indexes but possible k values. Then it does not start from 0 to max(p) - 1, but from 1 to max(p)
        res = r

        while l <= r:
            k = (l + r) // 2
            
            currHours = 0
            for pile in piles:
                currHours += ceil(pile / k)
            if currHours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res
