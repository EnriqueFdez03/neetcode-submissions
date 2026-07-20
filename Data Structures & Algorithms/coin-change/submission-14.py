class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [-1] * (amount + 1)

        def dfs(amount):
            if amount == 0:
                return 0
            if cache[amount] != -1:
                return cache[amount]
            
            numCoins = float('inf')
            for c in coins:
                if amount - c >= 0:
                    numCoins = min(1 + dfs(amount - c), numCoins)

            cache[amount] = numCoins
            return cache[amount]
        
        res = dfs(amount)
        return res if res != float('inf') else -1