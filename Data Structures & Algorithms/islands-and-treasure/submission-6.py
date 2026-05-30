class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        queue = deque([])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                (r, c) = queue.popleft()
                
                grid[r][c] = min(grid[r][c], dist)
                for dr, dc in directions:
                    rn = r + dr
                    cn = c + dc
                    if rn < 0 or cn < 0 or rn >= ROWS or cn >= COLS or grid[rn][cn] == -1 or (rn, cn) in visited:
                        continue
                    queue.append((rn, cn))
                    visited.add((rn, cn))
            dist += 1
                        
                        
        
        