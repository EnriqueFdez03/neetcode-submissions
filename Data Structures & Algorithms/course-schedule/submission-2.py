class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # applying Kahn algorithm, based on BFS. Topological sort
        # adjacency list
        adjList = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses # counts how many pre the node i has

        #INVERTED DICTIONARY
        for course, pre in prerequisites:
            adjList[pre].append(course)
            indegree[course] += 1
        
        # IDEA: Add first the nodes with no pre.
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # process the queue. FIRST those with indegree 0.
        count = 0
        while queue:
            course = queue.popleft()
            count += 1

            for next_course in adjList[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        return count == numCourses
