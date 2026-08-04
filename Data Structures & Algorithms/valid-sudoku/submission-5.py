class Solution:
    _SIZE = 9
    _SUBSIZE = 3

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colums = [set() for _ in range(self._SIZE)]

        for row in range(self._SIZE):
            currRow = set()
            for col in range(self._SIZE):
                num = board[row][col]
                if num == ".":
                    continue
                if num in colums[col] or num in currRow:
                    return False

                currRow.add(num)
                colums[col].add(num)

        for subRow in range(0, self._SIZE, self._SUBSIZE):
            for subCol in range(0, self._SIZE, self._SUBSIZE):
                subSquare = set()
                for row in range(subRow, subRow + self._SUBSIZE):
                    for col in range(subCol, subCol + self._SUBSIZE):
                        num = board[row][col]
                        if num == ".":
                            continue
                        if num in subSquare:
                            return False
                        
                        subSquare.add(num)
    
        return True
