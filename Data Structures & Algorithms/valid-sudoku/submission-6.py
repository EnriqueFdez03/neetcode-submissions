from collections import defaultdict

class Solution:
    _SIZE = 9
    _SUBSIZE = 3

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colums = [set() for _ in range(self._SIZE)]
        squares = defaultdict(set)

        for row in range(self._SIZE):
            currRow = set()
            for col in range(self._SIZE):
                num = board[row][col]
                if num == ".":
                    continue
                if num in colums[col] or num in currRow:
                    return False
                if num in squares[(row // 3, col // 3)]:
                    return False

                currRow.add(num)
                colums[col].add(num)
                squares[(row // 3, col // 3)].add(num)


        return True
