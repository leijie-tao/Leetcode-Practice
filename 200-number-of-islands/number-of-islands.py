class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return  #终止条件，行/列越界，或节点的值为0
            grid[r][c] = "0" #淹没当前位置，并dfs向四周扩散
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows): #遍历表中的每个位置
            for c in range(cols):
                if grid[r][c] == "1": #遇到陆地则计数，并以该位置为中心向四周淹没，直到边界或水域为止
                    count += 1
                    dfs(r, c)
        return count
