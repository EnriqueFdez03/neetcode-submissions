class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [-1] * len(s)
        def dfs(i):
            if i == len(s):
                return True
            if cache[i] != -1:
                return cache[i]
            
            for word in wordDict:
                length = len(word)
                if i + length <= len(s) and s[i:i + length] == word:
                    if dfs(i + length):
                        cache[i] = True
                        return cache[i]

            cache[i] = False     
            return cache[i]
        
        return dfs(0)