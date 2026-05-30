class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        acum = defaultdict(int)

        for num in nums:
            acum[num] += 1

        return [num for num, ocurr in sorted(acum.items(), key = lambda item:item[1], reverse=True)][:k]
            