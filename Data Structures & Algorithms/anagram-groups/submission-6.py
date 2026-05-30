from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aux = defaultdict(list)

        for word in strs:
            cons = [0] * 26
            for c in word:
                cons[ord(c) - ord('a')] += 1
            
            aux[tuple(cons)].append(word)
        
        return list(aux.values())