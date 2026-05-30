class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pacific = set((r, 0) for r in range(ROWS)) | set((0, c) for c in range(COLS))
        atlantic = set((ROWS - 1, c) for c in range(COLS)) | set((r, COLS - 1) for r in range(ROWS))

        res = []
        def findPath(r, c):
            touchesAtl = False
            touchesPac = False

            visited = set()
            def dfs(r, c):
                nonlocal touchesAtl, touchesPac
                visited.add((r, c))
                if (r, c) in pacific:
                    touchesPac = True
                if (r, c) in atlantic:
                    touchesAtl = True
                for dr, dc in directions:
                    rn = r + dr
                    cn = c + dc
                    if rn < 0 or cn < 0 or rn >= ROWS or cn >= COLS or (rn, cn) in visited or (touchesPac and touchesAtl) or heights[r][c] < heights[rn][cn]:
                        continue
                    dfs(rn, cn)
                
            dfs(r, c)
            if touchesAtl and touchesPac:
                res.append([r, c])
            
        for r in range(ROWS):
            for c in range(COLS):
                findPath(r, c)
                        
        return res