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
        def dfs(cur: TrieNode, i):
            print(cur.children.keys())
            if cur.isWord and i == len(word):
                return True
            if not cur or i >= len(word):
                return False

            c = word[i]
            res = False
            if word[i] != "." and word[i] in cur.children:
                return dfs(cur.children[word[i]], i + 1)
            elif word[i] == ".":
                for child in cur.children.keys():
                    res = res or dfs(cur.children[child], i + 1)
                    if res:
                        return res
            return False
        
        return dfs(self.root, 0)