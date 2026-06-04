class Solution:
    def decodeString(self, s: str) -> str:
        i = 0

        def decode():
            nonlocal i
            res = ""
            k = 0

            while i < len(s):
                c = s[i]

                if c.isdigit():
                    k = 10 * k + int(c)
                elif c == "[":
                    i += 1
                    res += k * decode()
                    k = 0
                elif c == "]":
                    return res
                else:
                    res += c

                i += 1    
            return res
        
        return decode()