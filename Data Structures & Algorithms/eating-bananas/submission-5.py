class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        minK = r
        while l <= r:
            k = (l + r) // 2
            
            hoursNeeded = 0
            for pile in piles:
                hoursNeeded += math.ceil(pile / k)
            
            if hoursNeeded <= h:
                minK = k
                r = k - 1
            else:
                l = k + 1
        
        return minK