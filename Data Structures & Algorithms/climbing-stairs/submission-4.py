class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def climbStairsAux(i):
            if i == n or i == n - 1:
                return 1
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = climbStairsAux(i + 1) + climbStairsAux(i + 2)
            return cache[i]
        
        return climbStairsAux(0)

    
    