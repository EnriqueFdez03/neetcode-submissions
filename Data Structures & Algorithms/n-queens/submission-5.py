class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(i, cols, diag1, diag2, path):
            if i == n:
                res.append(path.copy())
                return
            
            for j in range(n):
                if j in cols or j - i in diag1 or j + i in diag2:
                    continue
                
                cols.append(j)
                diag1.append(j - i)
                diag2.append(j + i)
                row = ["."] * n
                row[j] = "Q"
                path.append("".join(row))

                dfs(i + 1, cols, diag1, diag2, path)
                cols.pop()
                diag1.pop()
                diag2.pop()
                path.pop()
        
        dfs(0, [], [], [], [])
        return res