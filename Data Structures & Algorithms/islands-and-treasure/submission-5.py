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
                (r, c) = queue.popleft()
                
                visited.add((r, c))
                grid[r][c] = min(grid[r][c], dist)
                for dr, dc in directions:
                    if r + dr < 0 or c + dc < 0 or r + dr >= ROWS or c + dc >= COLS or grid[r + dr][c + dc] == -1 or (r + dr, c + dc) in visited:
                        continue
                    queue.append((r + dr, c + dc))
            dist += 1
                        
                        
        
        