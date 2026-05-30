class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort using kahn
        indegree = [0 for i in range(numCourses)]
        adj = { i:[] for i in range(numCourses)}
        
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
     
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)

            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return res if len(res) == numCourses else []