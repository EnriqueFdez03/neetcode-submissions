class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []
        
        if not digits:
            return []

        def dfs(i, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            if i >= len(digits):
                return
            
            corresp = mapping[digits[i]]
            for letter in corresp:
                path.append(letter)
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return res