class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.components = n
    
    def find(self, u):
        curr = self.parent[u]
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr   

    def union(self, u, v):
        parentU = self.find(u)
        parentV = self.find(v)
        if parentU == parentV:
            return False
        
        if self.rank[parentU] < self.rank[parentV]:
            self.parent[parentU] = parentV
        elif self.rank[parentV] > self.rank[parentU]:
            self.parent[parentV] = parentU
        else:
            self.parent[parentU] = parentV
            self.rank[parentV] += 1
        self.components -= 1
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        dsu = DSU(ROWS * COLS)

        zeroes = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                            dsu.union(r * COLS + c, nr * COLS + nc)
                else:
                    zeroes += 1

        return dsu.components - zeroes


