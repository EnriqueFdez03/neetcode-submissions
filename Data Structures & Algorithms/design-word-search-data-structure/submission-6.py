class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        def dfs(cur, i): # i pos of the word
            if i > len(word) - 1:
                return cur.isWord
            if not cur or i > len(word):
                return False

            if word[i] != ".":
                if word[i] not in cur.children:
                    return False
                
                cur = cur.children[word[i]]
                return dfs(cur, i + 1)
            else:
                for c in cur.children.values():
                    if dfs(c, i + 1):
                        return True
                return False

        return dfs(self.root, 0)