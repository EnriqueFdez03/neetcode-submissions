class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, u):
        cur = self.parent[u]
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]] # path halving O(alpha(n)) -> O(1)
            cur = self.parent[cur]
        return cur
    
    def union(self, u, v):
        parentU = self.find(u)
        parentV = self.find(v)
        if parentU == parentV:
            return False
        
        if self.rank[parentU] < self.rank[parentV]:
            self.parent[parentU] = parentV
        elif self.rank[parentV] < self.rank[parentU]:
            self.parent[parentV] = parentU
        else:
            self.parent[parentU] = parentV
            self.rank[parentV] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #minimum spanning tree -> kruskal
        edges = []
        for i in range(len(points)):
            x_i, y_i = points[i]
            for j in range(i, len(points)):
                x_j, y_j = points[j]
                dist = abs(x_i - x_j) + abs(y_i - y_j)
                edges.append((dist, i, j))
        
        edges.sort()
        dsu = DSU(len(points))
        total = 0
        for dist, u, v in edges:
            if dsu.union(u, v):
                total += dist
        
        return total
