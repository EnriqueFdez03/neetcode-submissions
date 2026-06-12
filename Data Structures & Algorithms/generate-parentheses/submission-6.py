class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, close, path):
            if close == n:
                res.append(path)
                return
            
            if open < n:
                path += "("
                dfs(open + 1, close, path)
                path = path[:-1]
            if close < open:
                path += ")"
                dfs(open, close + 1, path)
                path = path[:-1]
        
        dfs(0, 0, "")
        return res