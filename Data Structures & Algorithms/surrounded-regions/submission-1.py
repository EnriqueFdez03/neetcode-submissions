class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # dfs
        ROWS, COLS = len(board), len(board[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == "X" or board[r][c] == "N":
                return
            

            board[r][c] = "N"
            for dr, dc in directions:
                dfs(dr + r, dc + c)
            
            
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "N":
                    board[r][c] = "O"