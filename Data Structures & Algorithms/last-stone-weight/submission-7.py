import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-w for w in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            if x != y:
                heapq.heappush(maxHeap, -abs(x - y))
            
        return -maxHeap[0] if maxHeap else 0