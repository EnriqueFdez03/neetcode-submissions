class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, u):
        cur = self.parent[u]
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v): 
        parentU = self.find(u)
        parentV = self.find(v)
        if parentU == parentV:
            return False
        
        if self.rank[parentU] < self.rank[parentV]:
            self.parent[parentU] = parentV
        elif self.rank[parentU] > self.rank[parentV]:
            self.parent[parentV] = parentU
        else:
            self.parent[parentU] = parentV
            self.rank[parentV] += 1
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        ROWS, COLS = len(grid), len(grid[0])
        dsu = DSU(ROWS * COLS)
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                            if dsu.union(r * COLS + c, nr * COLS + nc):
                                islands -= 1

        return islands



        