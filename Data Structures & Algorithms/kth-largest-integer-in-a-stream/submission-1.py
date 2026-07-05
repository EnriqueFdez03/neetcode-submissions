import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [-num for num in nums]
        heapq.heapify(self.heap) 

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        
        aux = []
        i = 0
        while i != self.k:
            num = heapq.heappop(self.heap)
            aux.append(num)
            i += 1
        
        for num in aux:
            heapq.heappush(self.heap, num)

        return -aux[-1]
