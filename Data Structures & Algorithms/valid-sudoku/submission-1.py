class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        
        columns = [set() for _ in range(N)]
        for r in range(N):
            row = board[r]
            visited = set()
            for c in range(N):
                if row[c] == ".":
                    continue
                if row[c] in visited:
                    return False
                visited.add(row[c])
                
                if row[c] in columns[c]:
                    return False
                columns[c].add(row[c])

        for square in range(N):
            visited = set()
            for i in range(N // 3):
                for j in range(N // 3):
                    r = (square // 3) * 3 + i
                    c = (square % 3) * 3 + j
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in visited:
                        return False
                    visited.add(board[r][c])

        return True
