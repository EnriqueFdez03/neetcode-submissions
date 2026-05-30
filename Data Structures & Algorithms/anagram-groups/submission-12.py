from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramAgg = defaultdict(list)
        for word in strs:
            codifiedW = self.codifyString(word)
            anagramAgg[codifiedW].append(word)
        
        return [anagrams for anagrams in anagramAgg.values()]


    def codifyString(self, word: str) -> str:
        count = [0] * 26
        for l in word:
            count[ord(l) - ord("a")] += 1
        
        return tuple(count)
