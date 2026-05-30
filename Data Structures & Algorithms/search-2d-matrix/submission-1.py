class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # division to determine the row index and module to determine the column index

        width = len(matrix[0])
        height = len(matrix)
        size = height * width

        l = 0
        r = size - 1

        while l <= r:
            m = l + (r - l // 2)
            (i, j) = (m // width, m % width)
            item = matrix[i][j]
            if target < item:
                r = m - 1
            elif target > item:
                l = m + 1
            else:
                return True
        
        return False