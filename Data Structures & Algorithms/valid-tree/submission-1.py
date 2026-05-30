class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(n)}
        for u, v in edges:
            preMap[u].append(v)
            preMap[v].append(u)
        
        # a graph is a tree if there are no cicles
        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for child in preMap[node]:
                if child == parent:
                    continue

                if child in visited:
                    return False
    
                if not dfs(child, node):
                    return False

            return True
        
        if not dfs(0, -1):
            return False
        return len(visited) == n