class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        cols = [set() for _ in range(N)]
        squares = [set() for _ in range(N)]

        for i in range(N):
            row = set()
            for j in range(N):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row:
                    return False
                if board[i][j] in cols[j]:
                    return False
                
                squareIdx = (i // 3) * 3 + (j // 3) 
                if board[i][j] in squares[squareIdx]:
                    return False
                
                row.add(board[i][j])
                cols[j].add(board[i][j])
                squares[squareIdx].add(board[i][j])

        return True