class Solution:
    # state on i - dfs(i) - can s[i:] be segmented?
    # time complexity: 
    # There are up to n states * words * k (avg. length of words, slicing takes n time)
    # space - n states +. n (size of cache) -> n

    # let´s try bottom up approach. Construct solution from future ones
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        cache = [-1] * len(s)
        def dfs(i):
            if i == n:
                return True
            if cache[i] != -1:
                return cache[i]
            for w in wordDict:
                lenW = len(w)
                if i + lenW <= n and s[i: i + lenW] == w and dfs(i + lenW):
                    cache[i] = True
                    return cache[i]
            cache[i] = False
            return cache[i]
        
        return dfs(0)
