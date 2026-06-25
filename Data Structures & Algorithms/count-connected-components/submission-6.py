class DSU:
    def __init__(self, n):
        self.components = n
        self.rank = [1] * (n + 1)
        self.parent = [i for i in range(n)]

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur
    
    def union(self, u, v):
        parentU = self.find(u)
        parentV = self.find(v)
        if parentU == parentV:
            return # they are under the same component
        if self.rank[parentU] > self.rank[parentV]:
            self.parent[parentV] = parentU # as parentU has more rank than parentV, we link the component of V to U
        elif self.rank[parentV] < self.rank[parentU]:
            self.parent[parentU] = parentV
        else:
            self.parent[parentU] = parentV
            self.rank[parentV] += 1
        self.components -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = DSU(n)
        for u, v in edges:
            unionFind.union(u, v)

        return unionFind.components        