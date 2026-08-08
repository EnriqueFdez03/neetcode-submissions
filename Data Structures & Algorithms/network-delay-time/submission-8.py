import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra, is like bfs but with heap. Why: directed graph (could be undirected too) + starting point.
        adj = { i: [] for i in range(n + 1) }
        for u, v, w in times:
            adj[u].append((v, w))

        minH = [(0,k)] # we are starting at K, cost is 0
        visit = set()
        t = 0

        while minH:
            w1, n1 = heapq.heappop(minH)
            if n1 in visit: # needed, because a same node can exist several times in the minHeap. The one with lowest weight is the first that appears
                continue

            visit.add(n1)
            t = w1
            for n2, w2 in adj[n1]:
                if n2 not in visit: # do not add a nei we have already processed
                    heapq.heappush(minH, (w1 + w2, n2))
        
        return t if len(visit) == n else -1
