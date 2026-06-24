class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class Dictionary():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        ROWS, COLS = len(board), len(board[0])
        found = []
        visited = set()
        
        def backtrack(r, c, word, root):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or board[r][c] not in root.children:
                return False
            
            word += board[r][c]
            if root.children[board[r][c]].isWord and word:
                found.append(word)
                root.children[board[r][c]].isWord = False

            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                backtrack(nr, nc, word, root.children[board[r][c]])
            visited.remove((r, c))

        dictionary = Dictionary()
        for word in words:
            dictionary.insert(word)
        
        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, "", dictionary.root)
        return found

