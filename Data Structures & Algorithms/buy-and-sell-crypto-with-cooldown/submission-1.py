class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in cache:
                return cache[(i, canBuy)]

            cooldown = dfs(i + 1, canBuy)
            if canBuy:
                buy = dfs(i + 1, False) - prices[i]
                cache[(i, canBuy)] = max(buy, cooldown)
                return cache[(i, canBuy)]
            else:
                sell = dfs(i + 2, True) + prices[i]
                cache[(i, canBuy)] = max(sell, cooldown)
                return cache[(i, canBuy)]
            
        return dfs(0, True)