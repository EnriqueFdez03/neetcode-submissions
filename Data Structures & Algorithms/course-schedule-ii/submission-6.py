class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        
        queue = deque([])
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)

            for dependant in adj[curr]:
                indegree[dependant] -= 1
                if indegree[dependant] == 0:
                    queue.append(dependant)
        
        return order if len(order) == numCourses else []