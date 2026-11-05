class Solution:
    # --------- DFS: TC O(n^2)   SC O(n) --------
    # def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # n = len(isConnected)
        # visit = [False] * n
        # count = 0

        # # mark the city and its neighbors in visit
        # def dfs(city):
        #     visit[city] = True
        #     for neighbor in range(n):
        #         # if it's an unvisited adjacent city, mark all neighbors of it
        #         if isConnected[city][neighbor] == 1 and visit[neighbor] == False:
        #             dfs(neighbor)

        # for i in range(n):
        #     if not visit[i]:
        #         count += 1
        #         dfs(i)

        # return count



# --------- union-find: TC O(n^2)   SC O(n) --------
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # each node's root is itself, and each node is a province
        n = len(isConnected)
        root = list(range(n + 1))
        provinces = n

        # recursively look for the final root, and return it
        def find_root(node):
            # if root isn't the node itself, find the final root of this intermediate node
            if root[node] != node:
                root[node] = find_root(root[node])
            return root[node]
        
        # check if two nodes can be unioned. (same root -> don't need to union.    different root -> union two nodes with the same root)
        def can_union(node1, node2):
            nonlocal provinces
            root1, root2 = find_root(node1), find_root(node2)
            if root1 == root2:
                return False
            else:
                root[root2] = root1
                provinces -= 1
                return True

        # iterate each cell. if there is an edge, try to union
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    can_union(i, j)

        # the number of nodes that are not in the union -> a province
        return provinces
                
            
