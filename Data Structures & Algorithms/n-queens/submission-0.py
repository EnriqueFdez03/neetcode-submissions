class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def backtrack(i, cols, diag1, diag2, path): # i is row in which we are adding the n-queen
            if len(path) == n:
                res.append(["".join(row) for row in path])
                return
            
            for pos in range(n):
                # check if setting in i, pos is valid
                if pos in cols:
                    continue
                if i - pos in diag1:
                    continue
                if i + pos in diag2:
                    continue

                row = ["."] * n
                row[pos] = "Q"
                path.append(row)
                cols.add(pos)
                diag1.add(i - pos)
                diag2.add(i + pos)
                backtrack(i + 1, cols, diag1, diag2, path)
                path.pop()
                cols.remove(pos)
                diag1.remove(i - pos)
                diag2.remove(i + pos)
            
        backtrack(0, set(), set(), set(), [])
        return res