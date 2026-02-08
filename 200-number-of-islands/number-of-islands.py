#BFS解法
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, columns = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in range(columns)] for _ in range(rows)]
        count = 0

        #将第一个点的周边所有陆地都记录至访问表
        def dfs(r, c):
            visited[r][c] = True
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == "1" and visited[nr][nc] == False):
                    dfs(nr, nc) #节点在边界内、是陆地、还未标记，则对它展开搜查
        #遍历每行每列，寻找符合要求的陆地首点
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and visited[r][c] == False:
                    count += 1
                    dfs(r, c) #标记同一陆地的所有点
        
        return count



