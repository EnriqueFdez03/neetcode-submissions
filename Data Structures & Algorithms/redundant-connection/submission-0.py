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
            return False
        if self.rank[rootU] > self.rank[rootV]:
            self.parent[rootV] = rootU
        elif self.rank[rootV] > self.rank[rootU]:
            self.parent[rootU] = rootV
        else:
            self.parent[rootV] = rootU
            self.rank[rootU] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max(node for edge in edges for node in edge) + 1
        unionFind = DSU(n)

        for u, v in edges:
            if not unionFind.union(u, v):
                return [u, v]