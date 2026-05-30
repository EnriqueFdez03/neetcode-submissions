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
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        def backtrack(r, c, node: TrieNode, word):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or board[r][c] not in node.children:
                return

            word += board[r][c]
            if node.children[board[r][c]].isWord and word:
                res.append(word)
                node.children[board[r][c]].isWord = False

            visited.add((r,c))
            backtrack(r + 1, c, node.children[board[r][c]], word)
            backtrack(r - 1, c, node.children[board[r][c]], word)
            backtrack(r, c + 1, node.children[board[r][c]], word)
            backtrack(r, c - 1, node.children[board[r][c]], word)
            visited.remove((r,c))

        dictionary = Dictionary()
        for word in words:
            dictionary.insert(word)
        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, dictionary.root, "")
        
        return res