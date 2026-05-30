class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)
            
            right = dfs()
            left = dfs()

            if token == "+":
                return right + left
            if token == "-":
                return left - right
            if token == "*":
                return left * right
            if token == "/":
                return int(left / right)
            
        
        return dfs()