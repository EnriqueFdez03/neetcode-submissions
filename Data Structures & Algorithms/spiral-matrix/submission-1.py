class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        def dfs(row, col, r, c, dr, dc):
            if row == 0:
                return
            for i in range(col):
                r += dr
                c += dc
                res.append(matrix[r][c])
            dfs(col, row - 1, r, c, dc, -dr)
        
        dfs(len(matrix), len(matrix[0]), 0, -1, 0, 1)
        return res