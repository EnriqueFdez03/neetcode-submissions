class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Dictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def insertWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = []

        visited = set()
        def dfs(r, c, word, root):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r, c) in visited or board[r][c] not in root.children:
                return

            word += board[r][c]
            if root.children[board[r][c]].isWord and word:
                res.append(word)
                root.children[board[r][c]].isWord = False
            
            visited.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, word, root.children[board[r][c]])
            visited.remove((r, c))
            
        dictionary = Dictionary()
        for word in words:
            dictionary.insertWord(word)

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", dictionary.root)
        return res