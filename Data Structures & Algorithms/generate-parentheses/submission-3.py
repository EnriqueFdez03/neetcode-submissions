class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # decisions in each level, add "(" or ")"
        res = []

        def backtrack(opening, closing, curr):
            if len(curr) == n * 2:
                if validParentheses(curr):
                    res.append(curr)
                return

            if opening < n:
                backtrack(opening + 1, closing, curr + "(")
            if closing < opening:
                backtrack(opening, closing + 1, curr + ")")

        def validParentheses(s):
            stack = []
            closing = ")"

            for c in s:
                if c == closing:
                    if not stack:
                        return False
                    stack.pop()
                else:
                    stack.append("(")

            return len(stack) == 0
        
        backtrack(0, 0, "")
        return res
                    