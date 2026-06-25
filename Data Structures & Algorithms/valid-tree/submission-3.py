class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = { i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                if nei != parent and not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n