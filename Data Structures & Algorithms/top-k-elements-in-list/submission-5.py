from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        result = []

        for n in nums:
            counter[n] += 1
        
        heap = []
        for n, occ in counter.items():
            heapq.heappush(heap, (-occ, n))            

        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1

        return result