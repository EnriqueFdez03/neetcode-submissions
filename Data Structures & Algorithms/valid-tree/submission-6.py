class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = { i:[] for i in range(n) }

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(i, parent):
            if i in visited:
                return False
            
            visited.add(i)
            for nei in adj[i]:
                if nei != parent and not dfs(nei, i):
                    return False
            
            return True
        
        return dfs(0, 0) and len(visited) == n
        