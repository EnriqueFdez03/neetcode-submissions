class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatHours(rate):
            res = 0
            for pile in piles:
                res += math.ceil(pile / rate)
            
            return res

        minRate, maxRate = 1, max(piles)

        res = maxRate
        while minRate <= maxRate:
            rate = (minRate + maxRate) // 2
            currH = eatHours(rate)

            if currH <= h:
                res = rate
                maxRate = rate - 1
            else:
                minRate = rate + 1

        return res


