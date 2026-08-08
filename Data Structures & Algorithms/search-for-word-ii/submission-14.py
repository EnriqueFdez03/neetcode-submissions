class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Dictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        dictionary = Dictionary()
        for word in words:
            dictionary.insert(word)

        found = []
        visited = set()
        def dfs(r, c, curr, currWord):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] not in curr.children or (r, c) in visited:
                return False
            
            currWord += board[r][c]
            if curr.children[board[r][c]].isWord and currWord:
                found.append(currWord)
                curr.children[board[r][c]].isWord = False

            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, curr.children[board[r][c]], currWord)
            visited.remove((r,c))

        beginnings = set(word[0] for word in words)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in beginnings:
                    dfs(r, c, dictionary.root, "")

        return found