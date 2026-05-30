class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        cache = {}
        def dfs(i, cur):
            if cur == amount:
                return 1
            if cur > amount:
                return 0
            if (i, cur) in cache:
                return cache[(i, cur)]
            
            numCombinations = 0
            for j in range(i, n):
                if cur + coins[j] <= amount:
                    numCombinations += dfs(j, cur + coins[j])
            cache[(i, cur)] = numCombinations
            return numCombinations
        
        return dfs(0, 0)