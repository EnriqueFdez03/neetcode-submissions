class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU == rootV:
            return False # we are in the same component group
        if self.rank[rootU] > self.rank[rootV]:
            self.parent[rootV] = rootU
        elif self.rank[rootV] > self.rank[rootU]:
            self.parent[rootU] = rootV
        else:
            self.parent[rootV] = rootU
            self.rank[rootU] += 1 
        return True

    def isInSameComponent(self, u, v):
        return self.find(u) == self.find(v)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dsu = DSU(n * n)
        # think in the graph!! Vertices are connected to their nei. ThaT´S teh graph
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        positions = []
        for r in range(n):
            for c in range(n):
                positions.append((grid[r][c], r, c))
        positions.sort()

        for t, r, c in positions:
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= t:
                    dsu.union(r * n + c, nr * n + nc)
            if dsu.isInSameComponent(0, n * n - 1):
                return t

