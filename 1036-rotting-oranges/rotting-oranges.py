class Solution:
    # 多个点同时bfs扩散  ----> 先数出多少个烂橘子
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        q = deque()     # rotten oranges -> queue
        fresh = 0       # fresh oranges -> count to see when to stop

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:     # fresh > 0 防止最后一批入队(全部腐烂)后多算 minutes += 1
            n = len(q)
            for _ in range(n):
                r, c = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        q.append((new_r, new_c))
            minutes += 1
        
        if fresh == 0:
            return minutes
        else:
            return -1

