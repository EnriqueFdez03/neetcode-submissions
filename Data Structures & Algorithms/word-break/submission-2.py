class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        cache = {}
        def dfs(i, curr):
            if i == len(s):
                return curr == ""
            if (i, curr) in cache:
                return cache[(i, curr)]
            
            curr += s[i]
            res = dfs(i + 1, curr)
            if curr in words:
                res = res or dfs(i + 1, "")
            cache[(i, curr)] = res
            return res
            
        return dfs(0, "")