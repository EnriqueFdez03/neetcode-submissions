class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = { i:[] for i in range(numCourses) }
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            adjList[pre].append(course)
            indegree[course] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        while queue:
            curr = queue.popleft()
            count += 1

            for child in adjList[curr]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        return count == numCourses