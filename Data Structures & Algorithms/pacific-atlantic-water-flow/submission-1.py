class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(r, c, visited):    
            visited.add((r, c))
            for dr, dc in directions:
                rn, cn = r + dr, c + dc
                if rn < 0 or cn < 0 or rn >= ROWS or cn >= COLS or (rn, cn) in visited or heights[rn][cn] < heights[r][c]:
                    continue
                dfs(rn, cn, visited)

        pac = set()
        atl = set()
        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)
        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, atl)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))
                
        return res