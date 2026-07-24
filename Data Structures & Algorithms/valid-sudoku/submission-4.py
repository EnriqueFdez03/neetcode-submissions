class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        cols = [set() for _ in range(N)]

        for rowIdx in range(N):
            row = set()
            for colIdx in range(N):
                num = board[rowIdx][colIdx]
                if num == ".":
                    continue
                if num in row:
                    return False
                if num in cols[colIdx]:
                    return False
                
                row.add(num)
                cols[colIdx].add(num)

        for square in range(N):
            visited = set()
            for i in range(N // 3):
                for j in range(N // 3):
                    rowIdx = (square // 3) * 3 + i
                    colIdx = (square % 3) * 3 + j
                    num = board[rowIdx][colIdx]
                    if num == ".":
                        continue
                    if num in visited:
                        return False
                    
                    visited.add(num)
        
        return True
