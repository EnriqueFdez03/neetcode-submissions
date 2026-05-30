class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # EASY, just detect a cycle
        preMap = { i: [] for i in range(numCourses)}
        for curs, pre in prerequisites:
           preMap[curs].append(pre)
         
        visited = set()
        def dfs(node):
            if node in visited:
                return False # we detected a cycle
            if preMap[node] == []:
                return True

            visited.add(node)
            for pre in preMap[node]:
                if not dfs(pre):
                    return False
            preMap[node] = []
            visited.remove(node)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True



