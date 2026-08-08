class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = {node for edge in edges for node in edge}
        adj = {i: [] for i in range(len(nodes) + 1)}
        
        def dfs(i, parent):
            if i in visited:
                return True
            
            visited.add(i)
            for nei in adj[i]:
                if nei != parent and dfs(nei, i):
                    return True
            return False
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set()

            if dfs(u, -1):
                return [u, v]
                
        return res