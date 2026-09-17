# #----------------- DFS : m * n -------------------
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
#         rows, cols = len(grid), len(grid[0])
#         visit = [[False] * cols for _ in range(rows)]
#         count = 0
#         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#         def dfs(r, c):
#             if r not in range(rows) or c not in range(cols) or visit[r][c] == True or grid[r][c] == "0":
#                 return
#             visit[r][c] = True
#             for dr, dc in directions:
#                 dfs(r + dr, c + dc)

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and visit[r][c] == False:
#                     dfs(r, c)
#                     count += 1

#         return count






# ------------------ BFS: m * n  --------------------
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = [[False] * cols for _ in range(rows)]
        count = 0

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visit[r][c] = True
            while q:
                r, c = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    new_r = dr + r
                    new_c = dc + c
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == "1" and visit[new_r][new_c] == False:
                        q.append((new_r, new_c))
                        visit[new_r][new_c] = True

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and visit[r][c] == False:
                    bfs(r, c)
                    count += 1

        return count
        



