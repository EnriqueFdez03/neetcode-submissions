class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def backtrack(i, cols, diag1, diag2, path):
            if len(path) == n:
                res.append(["".join(row) for row in path])
                return

            for pos in range(n):
                if pos in cols:
                    continue
                if pos - i in diag1:
                    continue
                if pos + i in diag2:
                    continue

                row = ["."] * n
                row[pos] = "Q"
                path.append(row)
                cols.add(pos)
                diag1.add(pos - i)
                diag2.add(pos + i)
                backtrack(i + 1, cols, diag1, diag2, path)
                path.pop()
                cols.remove(pos)
                diag1.remove(pos - i)
                diag2.remove(pos + i)

        backtrack(0, set(), set(), set(), [])
        return res