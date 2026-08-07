class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, closed, path):
            if open == n and closed == n:
                res.append("".join(path))
                return
            
            if open < n: # (((
                path.append("(")
                dfs(open + 1, closed, path)
                path.pop()
            
            if open > closed:
                path.append(")")
                dfs(open, closed + 1, path)
                path.pop()
            
        dfs(0, 0, [])
        return res