class Solution:
    # state on i - dfs(i) - can s[i:] be segmented?
    # time complexity: 
    # There are up to n states * words * k (avg. length of words, slicing takes n time)
    # space - n states +. n (size of cache) -> n

    # let´s try bottom up approach. Construct solution from future ones
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
        
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        j = n
        for i in range(n - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= n and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]
