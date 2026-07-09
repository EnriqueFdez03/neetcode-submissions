class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):
            if grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0":
                    continue
                
                dfs(nr, nc)

        numIslands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    numIslands += 1
        
        return numIslands