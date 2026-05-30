class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            if remaining in cache:
                return cache[remaining]

            best = float('inf')
            for coin in coins:
                if coin <= remaining:
                    best = min(best, 1 + dfs(remaining - coin))
            cache[remaining] = best           
            return best

        res = dfs(amount)
        return res if res != float('inf') else -1
