#第一步：建图，网格本身即为邻接矩阵
#第二步：策略，dfs寻找所有路径，没找到返回0，找到向上返回1（计数）
#第三步：处理状态，“原为标记法”，标记访问过的为0
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, columns = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] == 0:
                return 0 #未找到：达到边界或当前点为0
            
            grid[r][c] = 0 #找到：淹没，计数1并加上四周的查找结果
            current_area = (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))
            return current_area
        
        for i in range(rows): #遍历图中每个格子，发现1时启动dfs，并更新最大值
            for j in range(columns):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
                
        return max_area