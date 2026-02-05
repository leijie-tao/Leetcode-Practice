#BFS解法
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows): #遍历表中的每个位置
            for c in range(cols):
                if grid[r][c] == "1": #遇到陆地则计数，把该起点入队，并淹没该起点（必须入队前淹没，否则可能被邻节点视为陆地重新入队）
                    count += 1
                    queue = deque([(r, c)])
                    grid[r][c] = "0"
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        #检查curr_r, curr_c的四个方向，如果是边界内且是陆地，则把该节点入队并淹没
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            next_r, next_c = curr_r + dr, curr_c + dc
                            if (0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == '1'):
                                queue.append((next_r, next_c))
                                grid[next_r][next_c] = "0"

        return count
