class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        i, j = 0, 1
        maxProfit = 0
        minWindow = i if prices[i] < prices[j] else j
        while j < len(prices):
            currProfit = prices[j] - prices[i]
            maxProfit = max(currProfit, maxProfit)
            minWindow = minWindow if prices[minWindow] < prices[j] else j
            j += 1
            i = minWindow
        
        return maxProfit