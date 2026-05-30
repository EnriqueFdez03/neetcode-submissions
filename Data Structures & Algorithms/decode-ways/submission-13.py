class Solution:
    def numDecodings(self, s: str) -> int:
        # how many ways can I decode the substring starting at s[i:]
        n = len(s)
        cache = [-1] * n
        def dfs(i):
            if i == n:
                return 1
            if cache[i] != -1:
                return cache[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if i < n - 1 and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)
            cache[i] = res
            return res
        return dfs(0)