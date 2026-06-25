class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # kahn algo -> indegre ? -> topological sort
        # dfs and detect that there are no cycles, states: 1, 2, 3.

        adj = { i: [] for i in range(numCourses) }

        for a, b in prerequisites:
            adj[a].append(b) # a depends on b
        
        states = [0] * numCourses # 0 not visited, 1 visiting, 2 visited
        def dfs(cur):
            if states[cur] != 0:
                return states[cur] == 1
            
            states[cur] = 1
            for nei in adj[cur]:
                if dfs(nei):
                    return True
            states[cur] = 2
            return False

        for i in range(numCourses):
            if dfs(i):
                return False
        return True
