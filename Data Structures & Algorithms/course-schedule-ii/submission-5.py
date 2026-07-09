class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # kahn algo
        adj = { i:[] for i in range(numCourses) }
        indegree = [0 for _ in range(numCourses)]

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        
        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
            
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)

            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei) 
        return res if len(res) == numCourses else []