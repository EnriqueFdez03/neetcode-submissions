class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set() # (r,c) pairs already visited

        def backtrack(r, c, i): # i is position in word
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or i >= len(word) or word[i] != board[r][c] or (r,c) in visited:
                return False
            
            if i == len(word) - 1 and board[r][c] == word[i]:
                return True
            
            visited.add((r,c))
            found = backtrack(r + 1, c, i + 1) or \
                backtrack(r - 1, c, i + 1) or \
                backtrack(r, c + 1, i + 1) or \
                backtrack(r, c - 1, i + 1)
            visited.remove((r,c))
            return found
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True
        return False