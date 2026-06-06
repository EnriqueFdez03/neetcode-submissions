import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            if task not in counts:
                counts[task] = 1
            else:
                counts[task] += 1
        
        heap = [(0, -c) for c in counts.values()]
            
        step = 0
        while heap:
            if heap[0][0] <= step:
                time, c = heapq.heappop(heap)
                c += 1
                if c != 0:
                    heapq.heappush(heap, (n + time + 1, c))
            
            step += 1

        return step
