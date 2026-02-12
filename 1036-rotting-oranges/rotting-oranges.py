class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        #初始化，收集所有烂橘子的位置，记录新鲜橘子的数量
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        if fresh_count == 0:
            return 0
        
        minutes = -1
        while queue: #所有烂橘子同时开始扩散
            minutes += 1 
            for _ in range(len(queue)): #弹出当前每个烂橘子，并查找他们的四周
                r, c = queue.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    # 如果四周在边界内，且有新鲜橘子，则变腐烂，并加入队列
                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
                        
        return minutes if fresh_count == 0 else -1


