class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dijkstra doesn´t work naturally here. Use bellmann ford for limiting by k steps and negative weights
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            tmp = prices.copy()

            for s, d, cost in flights:
                if prices[s] == float('inf'):
                    continue

                tmp[d] = min(tmp[d], prices[s] + cost)
            
            prices = tmp
        
        return prices[dst] if prices[dst] != float('inf') else -1