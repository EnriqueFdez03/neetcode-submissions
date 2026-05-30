import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distanceToOrigin(x, y):
            return math.sqrt(x**2 + y**2)
        
        distances = []
    
        for (x, y) in points:
            heapq.heappush(distances, [distanceToOrigin(x, y), x, y])
        
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(distances)
            res.append([x, y])
        return res