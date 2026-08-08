class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        # cuando se aplica el kahn algo, queremos saber sobre de cuántos pre course depende
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        coursed = 0
        while queue:
            course = queue.popleft()
            coursed += 1
            for dependant in adj[course]:
                indegree[dependant] -= 1
                if indegree[dependant] == 0:
                    queue.append(dependant)

        return coursed == numCourses