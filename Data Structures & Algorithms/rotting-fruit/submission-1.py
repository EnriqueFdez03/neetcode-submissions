class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        FRESH, ROTTEN = 1, 2
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        freshRemaining = 0
        queue = deque([])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == ROTTEN:
                    queue.append((i, j))
                elif grid[i][j] == FRESH:
                    freshRemaining += 1

        minutes = 0
        while queue and freshRemaining:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == FRESH:
                        freshRemaining -= 1
                        grid[nr][nc] = ROTTEN
                        queue.append((nr, nc))

        return minutes if not freshRemaining else -1