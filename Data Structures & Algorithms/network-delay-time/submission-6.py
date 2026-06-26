import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra O(E Log V)
        adj = {i: [] for i in range(n + 1)}
        for u, v, cost in times:
            adj[u].append((v, cost))

        minH = [(0, k)]
        visit = set()
        t = 0

        while minH:
            w1, n1 = heapq.heappop(minH)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minH, (w1 + w2, n2))
            
        return t if len(visit) == n else -1