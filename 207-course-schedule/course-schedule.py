class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses #初始化入度表：指向该节点的边的数量，记录当前课的先修课数量
        adjacency = [[] for _ in range(numCourses)] #初始化邻接表：记录依赖关系，记录该节点向后的路径
        for cur, pre in prerequisites: 
            indegrees[cur] += 1     #遍历构建：记录每个cur的入度+1
            adjacency[pre].append(cur)  #遍历构建：记录每个pre的邻接表

         # 拓扑排序：有向无环图 ——> 线性排序
        # 将所有入度为0的节点（不需要先修课）入队，队列为当前可修的课程
        lst = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                lst.append(i)
        queue = deque(lst)
       
        # 依次弹出当前可修(修完)的课程，并更新每个后继课程的入度表，寻找下一轮可修课程入队
        count = 0
        while queue:
            pre = queue.popleft()
            count += 1            
            for cur in adjacency[pre]:  
                indegrees[cur] -= 1 
                if indegrees[cur] == 0:
                    queue.append(cur)

        return count == numCourses #如果修完课程=总数，说明不存在“环”