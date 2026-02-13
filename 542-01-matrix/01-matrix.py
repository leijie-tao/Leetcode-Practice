class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, columns = len(mat), len(mat[0])
        dist = [[-1]* columns for _ in range(rows)] #访问表记录坐标值
        queue = deque()

        for r in range(rows):
            for c in range(columns):
                if mat[r][c] == 0:#以所有0为起点，记录访问值为0，并入队
                    dist[r][c] = 0 
                    queue.append((r,c))

        while queue:
            r, c = queue.popleft() #依次弹出0点，并查找四周
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < columns and dist[nr][nc] == -1:#如果新坐标在边界内且未被访问过
                    dist[nr][nc] = dist[r][c] + 1 #则新坐标的值 = 前坐标的值+1
                    queue.append((nr, nc)) 
        
        return dist