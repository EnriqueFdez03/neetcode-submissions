class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        corr = {"}" : "{", "]" : "[", ")" : "("}
        stack = []

        for c in s:
            if c in corr:
                if len(stack) == 0:
                    return False
                prev = stack.pop()
                if prev != corr[c]:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0