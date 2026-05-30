class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []

        def backtrack(i, curr): # pos of the digit
            if i == len(digits):
                if curr:
                    res.append(curr)
                return
            
            corr = mapping[digits[i]]
            for letter in corr:
                backtrack(i + 1, curr + letter)

        backtrack(0, "")
        return res