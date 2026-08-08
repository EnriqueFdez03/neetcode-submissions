class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if i == len(word):
                return curr.isWord
            if word[i] != "." and word[i] not in curr.children:
                return False
            
            if word[i] != ".":
                curr = curr.children[word[i]]
                if dfs(i + 1, curr):
                    return True
            else:
                for node in curr.children.values():
                    if dfs(i + 1, node):
                        return True
            
            return False
            
        return dfs(0, self.root)

