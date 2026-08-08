class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            adj[course].append(pre)
        
        res = []
        state = [0] * numCourses # 0 not visited, 1 visiting, 2 visited
        def dfs(course):
            if state[course] == 2:
                return True
            if state[course] == 1:
                return False
            
            state[course] = 1
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            res.append(course)
            state[course] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res