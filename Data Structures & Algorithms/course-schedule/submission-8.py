class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # kahn algo is similar to bfs but with indegree
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        
        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        processed = 0
        while queue:
            pre = queue.popleft()
            processed += 1
            for course in adj[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        return processed == numCourses
