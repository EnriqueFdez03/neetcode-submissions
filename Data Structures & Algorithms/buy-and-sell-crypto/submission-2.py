class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        maxProfit = 0
        i, j = 0, 1
        while i < j and j < len(prices):
            maxProfit = max(maxProfit, prices[j] - prices[i])
            if prices[i] >= prices[j]:
                i = j
            j += 1
        
        return maxProfit
            

            
