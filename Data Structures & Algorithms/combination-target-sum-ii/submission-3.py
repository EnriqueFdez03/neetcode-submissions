from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, path, curr): # whether we pick num_i or not
            if curr == target:
                res.append(path.copy())
                return
            
            if i >= len(candidates) or curr + candidates[i] > target:
                return
            
            path.append(candidates[i])
            backtrack(i + 1, path, curr + candidates[i]) # we pick it. BUT if we skip we need to skip all duplicates
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            path.pop()
            backtrack(i + 1, path, curr)
        
        backtrack(0, [], 0)
        return res