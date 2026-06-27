import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adj list

        adj = { i: [] for i in range(n + 1)}
        for u, v, t in times:
            adj[u].append((v, t))

        minH = [(0, k)]
        visited = set()
        sol = 0
        while minH:
            t, src = heapq.heappop(minH)
            if src in visited:
                continue
            visited.add(src)
            sol = t

            for dst, cost in adj[src]:
                if dst not in visited:
                    heapq.heappush(minH, (t + cost, dst))
        
        return sol if len(visited) == n else -1