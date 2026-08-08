class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def dfs(r, c, visited):            
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited or heights[r][c] > heights[nr][nc]:
                    continue
                
                dfs(nr, nc, visited)
            
        atl = set()
        pac = set()
        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, atl)
        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append((r, c))
        
        return res