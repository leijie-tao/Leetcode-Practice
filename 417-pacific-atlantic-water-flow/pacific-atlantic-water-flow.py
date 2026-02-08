class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, columns = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        can_reach_pacific = set() #维护两个海洋都能到达的集合，集合求交集
        can_reach_atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c)) #建立一个visited访问表（哈希集合），添加记录已经访问过的节点
            for dr, dc in directions: #遍历四个方向
                nr, nc = r + dr, c + dc #得到每个方向的新坐标
                if (0 <= nr < rows and 0 <= nc < columns and (nr, nc) not in visited and 
                        heights[nr][nc] >= heights[r][c]): #新坐标在边界内，新坐标不在访问表中，且新节点高度高于前节点
                    dfs(nr, nc, visited) #递归，添加新节点并查找新节点四周
        
        for r in range(rows): #遍历每行
            dfs(r, 0, can_reach_pacific)  #遍历最左侧一列（从太平洋开始灌水）      
            dfs(r, columns - 1, can_reach_atlantic) #遍历最右侧一列（从大西洋灌水）
        for c in range(columns): #遍历每列
            dfs(0, c, can_reach_pacific)  #遍历最上一排（太平洋）      
            dfs(rows - 1, c, can_reach_atlantic) #遍历最下一排（大西洋）

        return list(can_reach_pacific & can_reach_atlantic)
        