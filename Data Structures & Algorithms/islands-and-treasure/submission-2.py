class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque([])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        dist = 0
        visited = set()
        while queue:
            for _ in range(len(queue)):
                (rx, cx) = queue.popleft()
                if rx < 0 or cx < 0 or rx >= ROWS or cx >= COLS or grid[rx][cx] == -1 or (rx, cx) in visited:
                    continue
                visited.add((rx, cx))
                grid[rx][cx] = min(grid[rx][cx], dist)
                for dr, dc in directions:
                    queue.append((dr + rx, dc + cx))
            dist += 1
                        
                        
        
        