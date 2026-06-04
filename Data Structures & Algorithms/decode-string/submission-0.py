class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            
            else:
                cur = ""
                while stack and stack[-1] != "[":
                    cur = stack.pop() + cur
                
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(cur * int(k))
        
        return "".join(stack)