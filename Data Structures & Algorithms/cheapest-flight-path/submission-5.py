class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # this is bellmann ford. Use for shortest path with max length k or negative weights. Less efficient than dijkstra
        # O(V * E)
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            tmp = prices.copy()

            for s, d, cost in flights:
                if prices[s] == float('inf'):
                    continue
                
                tmp[d] = min(tmp[d], prices[s] + cost)
            prices = tmp
        
        return -1 if prices[dst] == float('inf') else prices[dst]