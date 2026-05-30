class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.components = n
    
    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]] # path optimization, to avoid linkedlists
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        parentU = self.find(u)
        parentV = self.find(v)
        if parentU == parentV:
            return False # they are already an union
        if self.rank[parentV] > self.rank[parentU]:
            self.parent[parentU] = parentV
        elif self.rank[parentU] > self.rank[parentV]:
            self.parent[parentV] = parentU
        else:
            self.parent[parentU] = parentV
            self.rank[parentU] += 1
        self.components -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = DSU(n)
        for u, v in edges:
            unionFind.union(u, v)
        
        return unionFind.components