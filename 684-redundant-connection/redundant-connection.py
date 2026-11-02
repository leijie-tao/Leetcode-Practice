class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        
        # check if there is a cycle, containing cur and target
        def hasCycle(cur, target, visit):
            if cur == target:
                return True
            # record current and check if unvisited neighbors can reach target
            visit.add(cur)
            for neighbor in adj[cur]:
                if neighbor not in visit:
                    if hasCycle(neighbor, target, visit):
                        return True
            return False

        # add edges one by one
        for u, v in edges:
            # have to create the set outside and pass it into dfs, so that all layers of dfs can share the set
            visit = set()
            if hasCycle(u, v, visit):
                return [u, v]
            adj[u].append(v)
            adj[v].append(u)

        return []
