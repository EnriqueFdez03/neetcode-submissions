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
            for w in words:
                if s[i: i + len(w)] == w and dfs(i + len(w)):
                    cache[i] = True
                    return True
            cache[i] = False
            return False

        return dfs(0)           