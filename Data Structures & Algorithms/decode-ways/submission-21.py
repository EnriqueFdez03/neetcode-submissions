class Solution:
    # let i can s[i:] be decoded
    def numDecodings(self, s: str) -> int:
        cache = [-1] * len(s)

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if cache[i] != -1:
                return cache[i]
            
            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)
            cache[i] = res
            
            return res
        
        return dfs(0)