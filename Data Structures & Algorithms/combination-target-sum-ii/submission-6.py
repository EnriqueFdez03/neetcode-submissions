from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, currSum, path):
            if currSum == target:
                res.append(path.copy())
                return

            if i >= len(candidates) or currSum > target:
                return
            
            path.append(candidates[i])
            dfs(i + 1, currSum + candidates[i], path)
            path.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, currSum, path)
 
        dfs(0, 0, [])
        return res

        '''
        dfs(0, 0, []) -> dfs(1, 1, [1]) -> dfs(2, 3, [1, 2]) -> dfs(3, 6, [1, 2, 3]) -> dfs(4, 10, [1, 2, 3, 4]) -> X
                                                             -> dfs(3, 3, [1, 2]) -> dfs(4, 7, [1, 2, 4])
        '''