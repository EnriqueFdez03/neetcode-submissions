class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        acum = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            acum[sortedS].append(s)

        return list(acum.values())



    