class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zeroCols = set()
        zeroRows = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)
        
        print(zeroCols)
        print(zeroRows)
        for i in zeroRows:
            for j in range(cols):
                matrix[i][j] = 0
        for i in range(rows):
            for j in zeroCols:
                matrix[i][j] = 0