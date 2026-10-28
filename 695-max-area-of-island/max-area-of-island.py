class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # 1. record status with 'visit'
        rows, cols = len(grid), len(grid[0])
        visit = [[False] * cols for _ in range(rows)]
        # 2. record adjacency
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # 3. result aggregation
        max_area = 0

        # 4.search process
        def dfs(r, c):
            nonlocal area
            if r not in range(rows) or c not in range(cols) or visit[r][c] == True or grid[r][c] == 0:
                return
            visit[r][c] = True
            area += 1
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # 5. apply to each cell
        for r in range(rows):
            for c in range(cols):
                if visit[r][c] == False and grid[r][c] == 1:
                    area = 0    # ❗️use a global variable and accumulate it in dfs recursion
                    dfs(r, c)
                    max_area = max(max_area, area)

        return max_area

        
        
        
    # #  ------ Refine: sink the island after visiting --------
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:      
        # if not grid:
        #     return 0
        # rows, columns = len(grid), len(grid[0])
        # max_area = 0

        # def dfs(r, c):
        #     if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] == 0:
        #         return 0 #未找到：达到边界或当前点为0
            
        #     grid[r][c] = 0 #找到：淹没，计数1并加上四周的查找结果
        #     current_area = (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))
        #     return current_area
        
        # for i in range(rows): #遍历图中每个格子，发现1时启动dfs，并更新最大值
        #     for j in range(columns):
        #         if grid[i][j] == 1:
        #             max_area = max(max_area, dfs(i, j))
                
        # return max_area