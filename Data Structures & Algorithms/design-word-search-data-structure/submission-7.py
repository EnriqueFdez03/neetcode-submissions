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
        curr = self.root

        def dfs(i, curr): # i is the current pos we are searching
            if i == len(word):
                return curr.isWord

            c = word[i]
            if c != ".":
                if c not in curr.children:
                    return False
                curr = curr.children[c]
                return dfs(i + 1, curr)
            
            for c in curr.children.keys():
                if dfs(i + 1, curr.children[c]):
                    return True
                    
            return False
        
        return dfs(0, curr)