class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # decisions in each level, add "(" or ")"
        res = []

        def backtrack(opening, closing, curr):
            if len(curr) == n * 2:
                res.append(curr)

            if opening < n:
                backtrack(opening + 1, closing, curr + "(")
            if closing < opening:
                backtrack(opening, closing + 1, curr + ")")

        backtrack(0, 0, "")
        return res
                    