class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        queue = deque([])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))

        distance = 0      
        while queue:
            for _ in range(len(queue)):
                (r, c) = queue.popleft()
                grid[r][c] = min(grid[r][c], distance)

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[r + dr][c + dc] != INF:
                        continue
                    queue.append((nr,nc))
            distance += 1