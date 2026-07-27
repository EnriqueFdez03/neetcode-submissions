class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif c == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(float(a) / b))
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(c))
        
        return stack[0]