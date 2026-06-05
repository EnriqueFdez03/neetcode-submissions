class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {'+', '-', '*', "/"}
        stack = []

        for c in tokens:
            if c not in operands:
                stack.append(int(c))
            else:
                res = 0
                b, a = stack.pop(), stack.pop()
                if c == "+":
                    stack.append(a + b)
                elif c == "-":
                    stack.append(a - b)
                elif c == "*":
                    stack.append(a * b)
                else: # /
                    stack.append(int(a / b))
            
        return stack.pop()