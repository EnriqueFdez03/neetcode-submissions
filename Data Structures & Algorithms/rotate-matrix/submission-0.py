class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        00 01.   10 00
        10 11    11 01


        '''
        l, r = 0, len(matrix) - 1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1

        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]