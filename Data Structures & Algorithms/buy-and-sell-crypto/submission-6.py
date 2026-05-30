class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, i = 0, 0
        while i < len(prices):
            j = i
            while j < len(prices) and prices[j] >= prices[i]:
                res = max(res, prices[j] - prices[i])
                j += 1
            i = j
        
        return res
