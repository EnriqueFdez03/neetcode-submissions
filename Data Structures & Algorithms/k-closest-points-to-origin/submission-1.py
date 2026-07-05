import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x_i, y_i in points:
            dist = math.sqrt(x_i**2 + y_i**2)
            heapq.heappush(minHeap, (-dist, [x_i, y_i]))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
            
        return [point for _, point in minHeap]
