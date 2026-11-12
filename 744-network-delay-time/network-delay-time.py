class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # adjacency list records neighbor and weights {u: (v, w)}
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        # status: the shortest distance to node k
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        min_heap = [(0, k)]     #use mini heap to get shortest path

        while min_heap:
            cur_time, u = heapq.heappop(min_heap)
            # make sure dist records shortest distance
            if cur_time > dist[u]:
                continue
            # If find a shorter path, iterate every neighbor
            for v, w in adj[u]:
                new_time = cur_time + w
                # update shortest distance to neighbor, and push neighbor into heap
                if new_time < dist[v]:
                    dist[v] = new_time
                    heapq.heappush(min_heap, (new_time, v))
        
        max_delay = max(dist[1:])
        if max_delay < float('inf'):
            return max_delay
        else:
            return -1