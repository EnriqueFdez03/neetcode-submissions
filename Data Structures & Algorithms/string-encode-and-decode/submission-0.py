class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for word in strs:
            encodedStr += f"{len(word)}#{word}"
        return encodedStr

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            
            i = j + 1
            word = s[i:i+length]
            res.append(word)
            i = i + length
        
        return res
                