class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # state based on a. Minimum amount of coins required for reaching a
        cache = {}
        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            if rem in cache:
                return cache[rem]
            
            res = float('inf')
            for coin in coins:
                res = min(res, 1 + dfs(rem - coin))
            
            cache[rem] = res
            return res
        
        res = dfs(amount)
        return res if res != float('inf') else -1


         
