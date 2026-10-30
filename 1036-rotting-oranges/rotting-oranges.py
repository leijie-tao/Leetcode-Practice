class Solution:
    # iterate by layer --> BFS    TC:O(m*n)   SC:O(m*n)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        # adjacent list: 4 directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh = 0
        time = 0
        #iterate each cell, add all rotted oranges into queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        # While the queue is not empty and fresh oranges exist
        while q and fresh > 0:
            n = len(q)
            time += 1
            # check 4 neighbors of each rotten orange -> make fresh orange rotten
            for _ in range(n):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
        
        if fresh == 0:
            return time
        else:
            return -1



