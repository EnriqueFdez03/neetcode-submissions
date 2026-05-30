class Solution:
    def climbStairs(self, n: int) -> int:
        memory = [-1] * (n + 1)
        def dfs(i):
            if i <= 3:
                return i
            if memory[i] != -1:
                return memory[i]

            memory[i] = dfs(i - 1) + dfs(i - 2)
            return memory[i]
        
        return dfs(n)