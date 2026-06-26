class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]] # path halving
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskal is DSU + sorting
        n = len(points)
        dsu = DSU(n)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        
        edges.sort(key=lambda x: x[0])
        minCost = 0
        for dist, u, v in edges:
            if dsu.union(u, v):
                minCost += dist
        return minCost