class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)

        cache = {}
        def dfs(i, amount): 
            if amount == 0:
                return 1
            if amount < 0 or i >= n:
                return 0
            if (i, amount) in cache:
                return cache[(i, amount)]
            
            res = dfs(i, amount - coins[i])
            newIdx = i + 1
            while newIdx < n and coins[newIdx - 1] == coins[newIdx]:
                newIdx += 1
            res += dfs(newIdx, amount)
            
            cache[(i, amount)] = res
            return res
        
        return dfs(0, amount)
