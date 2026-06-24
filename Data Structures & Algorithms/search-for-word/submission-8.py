class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def backtrack(r, c, i, visited):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or i >= len(word) or board[r][c] != word[i] or (r,c) in visited:
                return False
            if i == len(word) - 1:
                return True
            
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if backtrack(nr, nc, i + 1, visited):
                    return True
            visited.remove((r, c))
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and backtrack(r, c, 0, set()):
                    return True
        return False