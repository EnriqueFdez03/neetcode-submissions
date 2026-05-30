class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create the adjancency list
        adjList = { i:[] for i in range(numCourses)}
        for curs, pre in prerequisites:
            adjList[curs].append(pre)

        states = [0] * numCourses
        def dfs(node):
            if states[node] == 2:
                return True
            if states[node] == 1:
                return False
            
            states[node] = 1
            for pre in adjList[node]:
                if not dfs(pre):
                    return False
            states[node] = 2
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True