class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [-1] * (amount + 1)
        
        def dfs(amount):
            if amount == 0:
                return 0
            if cache[amount] != -1:
                return cache[amount]
            
            count = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    count = min(count, 1 + dfs(amount - coin))
            cache[amount] = count
            return count

        res = dfs(amount)        
        return res if res != float('inf') else -1
