class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        closeToOpen = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        
        for c in s:
            if c in closeToOpen.values():
                stack.append(c)
            elif c in closeToOpen:
                if not stack or stack[-1] != closeToOpen[c]:
                    return False
                stack.pop()
            else:
                return False

        return not stack