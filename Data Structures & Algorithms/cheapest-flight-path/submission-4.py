class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # this is dijkstra -> like bfs but with heaps
        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        adj = {i: [] for i in range(n)}
        for u, v, cost in flights:
            adj[u].append((v, cost))

        dist[src][0] = 0
        minH = [(0, src, -1)] # cost, node, nº of stops

        while minH:
            cost, node, stops = heapq.heappop(minH)
            if dst == node:
                return cost
            if stops == k or dist[node][stops + 1] < cost:
                continue
            for nei, w in adj[node]:
                if dist[nei][stops + 2] > cost + w:
                    dist[nei][stops + 2] = cost + w
                    heapq.heappush(minH, (cost + w, nei, stops + 1))
        return -1