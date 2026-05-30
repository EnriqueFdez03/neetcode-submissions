# Implementing kruskal
# kruskal relies on DSU
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, node):        
        cur = node
        while self.parent[cur] != cur:
            self.parent[node] = self.parent[self.parent[node]] # path opt
            cur = self.parent[cur]
        return cur
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU == rootV:
            return False # already form part of the same group
        if self.rank[rootU] > self.rank[rootV]:
            self.parent[rootV] = rootU
        elif self.rank[rootV] > self.rank[rootU]:
            self.parent[rootU] = rootV
        else:
            self.parent[rootV] = rootU
            self.rank[rootU] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        
        edges.sort() # sort!!! here it comes kruskal. SORT
        res = 0
        for dist, u, v in edges:
            if dsu.union(u, v):
                res += dist
        return res




