class Solution:
    ## -------- TC: O(N^2)   SC: O(N) ---------
    # def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # n = len(edges)
        # adj = [[] for _ in range(n + 1)]
        
        # # check if there is a cycle, containing cur and target
        # def hasCycle(cur, target, visit):
        #     if cur == target:
        #         return True
        #     # record current and check if unvisited neighbors can reach target
        #     visit.add(cur)
        #     for neighbor in adj[cur]:
        #         if neighbor not in visit:
        #             if hasCycle(neighbor, target, visit):
        #                 return True
        #     return False

        # # add edges one by one
        # for u, v in edges:
        #     # have to create the set outside and pass it into dfs, so that all layers of dfs can share the set
        #     visit = set()
        #     if hasCycle(u, v, visit):
        #         return [u, v]
        #     adj[u].append(v)
        #     adj[v].append(u)

        # return []
    
    
    # ------Optimal: union-find   TC & SC: O(N)------------
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        root = list(range(n + 1))   # root[i] = i

        def find_root(node):
            if root[node] != node:
                root[node] = find_root(root[node])  #path compression
            return root[node]   # node is the root
        
        for node1, node2 in edges:
            root1, root2 = find_root(node1), find_root(node2)
            # two nodes have the same root --> redundant edge
            if root1 == root2:
                return [node1, node2]   
            # two nodes don't connect --> union: all regard root1 as root
            else:
                root[root2] = root1

        
