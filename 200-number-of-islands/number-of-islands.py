#DFS解法
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        used = [[False] * cols for _ in range(rows)]
        res = 0

        # DFS visit all cells around (r,c), and mark them as used
        def dfs(r, c):
            # Stop condition: 1-2.out of range  3.visited  4.meet water
            if r not in range(rows) or c not in range(cols) or used[r][c] == True or grid[r][c] == "0":
                return
            used[r][c] = True
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in direction:
                dfs(r + dr, c + dc)


        for r in range(rows):
            for c in range(cols):
                # If it's a new island, start DFS
                if grid[r][c] == "1" and used[r][c] == False:
                    dfs(r, c)
                    res += 1
        return res



        # def bfs(r, c):
        #     q = deque([(r, c)])      # [tuple]
        #     used[r][c] = True
        #     while q:
        #         cr, cc = q.popleft()
        #         direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        #         for dr, dc in direction:
        #             nr, nc = cr + dr, cc + dc
                      ## Add valid cells into queue to search for their neighbors
        #             if (0 <= nr < rows and
        #              0 <= nc < col and
        #               used[nr][nc] == False and
        #                grid[nr][nc] == "1"):
        #                 used[nr][nc] = True
        #                 q.append((nr, nc))


