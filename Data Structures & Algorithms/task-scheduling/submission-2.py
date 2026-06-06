import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            if task not in counts:
                counts[task] = 1
            else:
                counts[task] += 1
        
        heap = []
        for task in counts.keys():
            heapq.heappush(heap, (0, -counts[task], task))
    
        step = 0
        while heap:
            if heap[0][0] <= step:
                time, _, task = heapq.heappop(heap)
                counts[task] -= 1
                if counts[task] > 0:
                    heapq.heappush(heap, (n + time + 1, -counts[task], task))
            
            step += 1

        return step
