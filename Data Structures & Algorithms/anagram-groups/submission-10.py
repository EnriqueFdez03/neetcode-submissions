class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        acum = defaultdict(list)
        for word in strs:
            vector = self.wordToVector(word)
            acum[vector].append(word)
        
        return list(acum.values())

    def wordToVector(self, word: str) -> str:
        res = [0] * 26

        for c in word:
            res[ord(c) - ord('a')] += 1

        return tuple(res)