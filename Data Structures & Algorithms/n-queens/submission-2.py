class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def backtrack(i, cols, diag1, diag2, path):
            if len(path) == n:
                res.append(path[:])
            
            for j in range(n):
                if j in cols:
                    continue
                if j - i in diag1:
                    continue
                if j + i in diag2:
                    continue
                
                row = ["."] * n
                row[j] = "Q"
                path.append("".join(row))
                cols.add(j)
                diag1.add(j - i)
                diag2.add(j + i)

                backtrack(i + 1, cols, diag1, diag2, path)
                cols.remove(j)
                diag1.remove(j - i)
                diag2.remove(j + i)
                path.pop()
            
        backtrack(0, set(), set(), set(), [])
        return res
            
            
