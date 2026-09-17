class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = [[False] * cols for _ in range(rows)]
        shapes = set()  #set() save relative corrdinate
        count = 0
        
        #dfs(r, c, r0, c0, shape) to record the shape: stop, mark, 4 directions
        def dfs(r, c, r0, c0, shape:list):
            if r not in range(rows) or c not in range(cols) or visit[r][c] or grid[r][c] == 0:
                return
            visit[r][c] = True
            shape.append((r - r0, c - c0))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, r0, c0, shape)

        # dfs each cell, record new island shape
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visit[r][c] == False:
                    shape = []
                    dfs(r, c, r, c, shape)
                    if tuple(shape) not in shapes:
                        count += 1
                        shapes.add(tuple(shape))

        return count

        