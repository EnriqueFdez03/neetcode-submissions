import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x_i, y_i in points:
            dist = math.sqrt(x_i**2 + y_i**2)
            heapq.heappush(maxHeap, (-dist, [x_i, y_i]))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
            
        return [point for _, point in maxHeap]
