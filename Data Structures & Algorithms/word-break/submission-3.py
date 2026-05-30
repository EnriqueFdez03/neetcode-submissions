class Solution:
    # state on i - dfs(i) - can s[i:] be segmented?
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        cache = {}

        def dfs(i):
            if i == n:
                return True
            if i in cache:
                return cache[i]
            for j in range(i + 1, n + 1): # till n
                if s[i:j] in words and dfs(j):
                    cache[i] = True
                    return True
            cache[i] = False
            return False

        return dfs(0)           