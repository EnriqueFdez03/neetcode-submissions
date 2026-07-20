class Solution:
    # let i we can decode the string s[i:]
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [-1] * len(s)
        def dfs(i):
            if i == len(s):
                return True
            if cache[i] != -1:
                return cache[i]

            for w in wordDict:
                lenW = len(w)
                if i + lenW <= len(s) and s[i: i + lenW] == w:
                    if dfs(i + lenW):
                        cache[i] = True
                        return cache[i]
            cache[i] = False
            return False
        
        return dfs(0)
                         