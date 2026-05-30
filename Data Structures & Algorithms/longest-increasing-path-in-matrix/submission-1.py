class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        cache = [[-1] * COLS for _ in range(ROWS)]
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0
            if cache[r][c] != -1:
                return cache[r][c]
            
            longest = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and matrix[r][c] < matrix[nr][nc]:
                    longest = max(longest, 1 + dfs(nr, nc))
            cache[r][c] = longest
            return cache[r][c]
        
        longest = 1
        for i in range(ROWS):
            for j in range(COLS):
                longest = max(longest, dfs(i, j))
            
        return longest