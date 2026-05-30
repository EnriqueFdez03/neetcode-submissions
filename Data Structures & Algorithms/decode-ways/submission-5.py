class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        n = len(s)

        def dfs(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            if i in cache:
                return cache[i]

            # take one digit
            res = dfs(i + 1)

            # take two digits if valid
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6")):
                res += dfs(i + 2)

            cache[i] = res
            return res

        return dfs(0)