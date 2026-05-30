class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dfs(i, amount): # takes the ith floor
            if i >= len(cost):
                return amount
            if (i, amount) in cache:
                return cache[(i, amount)]
            
            cache[(i, amount)] = min(dfs(i + 1, cost[i] + amount), dfs(i + 2, cost[i] + amount))
            return cache[(i, amount)]

        return min(dfs(0, 0), dfs(1, 0))