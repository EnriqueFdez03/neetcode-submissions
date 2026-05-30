class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # state based on a. Minimum amount of coins required for reaching a
        cache = {}
        def dfs(rem, count):
            if (rem, count) in cache:
                return cache[(rem, count)]
            if rem == 0:
                return count
            if rem < 0:
                return float('inf')
            
            res = float('inf')
            for coin in coins:
                res = min(res, dfs(rem - coin, count + 1))
            
            cache[(rem, count)] = res
            return res
        
        res = dfs(amount, 0)
        return res if res != float('inf') else -1


         
