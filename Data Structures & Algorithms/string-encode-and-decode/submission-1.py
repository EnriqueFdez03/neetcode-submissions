class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            length = len(word)
            res.append(f"{length}#{word}")

        return "".join(res)

    # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            
            j += 1 # word starting point
            res.append(s[j:j+length])
            i = j + length
        
        return res

