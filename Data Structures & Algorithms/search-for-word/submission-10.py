class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(r, c, i, visited):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or i >= len(word) or board[r][c] != word[i] or (r, c) in visited:
                return False
            
            visited.add((r, c))
            if i == len(word) - 1:
                return True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if dfs(nr, nc, i + 1, visited):
                    return True
            
            visited.remove((r, c))
            return False
             
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0, set()):
                    return True
        
        return False
