class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visit = [False] * n
        count = 0

        # mark the city and its neighbors in visit
        def dfs(city):
            visit[city] = True
            for neighbor in range(n):
                # if it's an unvisited adjacent city, mark all neighbors of it
                if isConnected[city][neighbor] == 1 and visit[neighbor] == False:
                    dfs(neighbor)

        for i in range(n):
            if not visit[i]:
                count += 1
                dfs(i)

        return count
