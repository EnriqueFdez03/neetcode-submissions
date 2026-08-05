class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            r += 1

        return maxProfit