class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        def dfs(r, c):
            #触发边缘的条件：出界或者遇到水
            if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] == 0:
                return 1
            #遇到已访问过的陆地，不再重复搜查其周边。修改数值标记已访问。
            if grid[r][c] == 2:
                return 0
            grid[r][c] = 2
            return (dfs(r+1,c) + dfs(r-1,c) + dfs(r, c+1) + dfs(r, c-1))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    return dfs(r, c)
        