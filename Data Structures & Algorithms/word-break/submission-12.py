class Solution:
    # let i we can decode the string s[i:]
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [-1] * len(s)

        def dfs(i):
            if i == len(s):
                return True
            if i > len(s):
                return False
            if cache[i] != -1:
                return cache[i]

            for word in wordDict:
                lenW = len(word)
                if s[i: i + lenW] == word:
                    if dfs(i + lenW):
                        return True
            
            cache[i] = False
            return cache[i]
        
        return dfs(0)