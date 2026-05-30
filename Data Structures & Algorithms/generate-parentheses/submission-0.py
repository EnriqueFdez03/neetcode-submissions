class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # decisions in each level, add "(" or ")"
        res = []

        def backtrack(curr):
            if len(curr) == n * 2:
                if validParentheses(curr):
                    res.append(curr)
                return

            backtrack(curr + "(")
            backtrack(curr + ")")

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
        
        backtrack("")
        return res
                    