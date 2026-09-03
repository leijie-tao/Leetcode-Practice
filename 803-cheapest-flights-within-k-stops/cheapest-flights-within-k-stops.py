class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        # Save the cheapest price of reaching a city from src
        dist = [INF] * n
        dist[src] = 0

        for _ in range(k + 1):
            temp = dist[:]          
            for u, v, w in flights:
                # If u is accessible, and previous price + flight price < current cheapest price to v
                if dist[u] != INF and dist[u] + w < temp[v]:
                    temp[v] = dist[u] + w
            dist = temp

        # Return the price which has valid flights
        if dist[dst] != INF:
            return dist[dst] 
        else:
            return -1