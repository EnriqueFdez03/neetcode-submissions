class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # clearly bfs
        ROWS, COLS = len(grid), len(grid[0])
        FRESH, ROTTEN = 1, 2
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        numBananas = sum(b != 0 for r in grid for b in r)
        
        queue = deque([])
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == ROTTEN:
                    queue.append((r, c))
                elif grid[r][c] == FRESH:
                    fresh += 1
        
        minutes = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == FRESH:
                        grid[nr][nc] = ROTTEN
                        queue.append((nr, nc))
                        fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1