class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = { i: [] for i in range(n)}

        for a1, b1 in edges:
            adjList[a1].append(b1)
            adjList[b1].append(a1)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in adjList[node]:
                if nei in visited:
                    continue

                dfs(nei)
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
            
        return count