class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = "+-*/"
        
        def dfs():
            c = tokens.pop()

            if c not in operands:
                return int(c)
            
            operand = c

            b = dfs()
            a = dfs()

            if operand == "+":
                return a + b
            elif operand == "-":
                return a - b
            elif operand == "*":
                return a * b
            else: # /
                return int(a / b)
        
        return dfs()