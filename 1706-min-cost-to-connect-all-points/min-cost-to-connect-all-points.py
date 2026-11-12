class Solution:
    #----- Prim Algorithm   TC:O(N^2)  SC:O(N) ---------
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        # The distance of each point reaching connection
        dist = [float('inf')] * n
        dist[0] = 0
        visit = [False] * n
        total_cost = 0

        # Find the nearest point each time, and upadte visit & cost
        for _ in range(n):
            u = -1
            for i in range(n):
                if visit[i] == False and (u == -1 or dist[i] < dist[u]):
                    u = i   # u is the nearest point to connection
            visit[u] = True
            total_cost += dist[u]

            # Update the distance list of other unvisited points since u joined the connection
            x, y = points[u]
            for v in range(n):
                if not visit[v]:
                    d = abs(x - points[v][0]) + abs(y - points[v][1])
                    if d < dist[v]:
                        dist[v] = d
        
        return total_cost
