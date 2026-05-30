class Solution:
    # let i can s[i:] be decoded
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cache = [-1] * n
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if cache[i] != -1:
                return cache[i]
            
            if s[i] == "0":
                cache[i] = 0
                return cache[i]
            
            res = dfs(i + 1)
            if s[i] == "1" or (i < n - 1 and s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)
            cache[i] = res
            return cache[i]
        
        return dfs(0)