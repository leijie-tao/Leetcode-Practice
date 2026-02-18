class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses #入度表：指向该节点的边的数量，记录当前课的先修课数量
        adjacency = [[] for _ in range(numCourses)] #邻接表：记录当前课后可以修的课
        for cur, pre in prerequisites: 
            indegrees[cur] += 1     #想修cur,必须先修pre,入读表记+1
            adjacency[pre].append(cur)  #添加邻接表内pre后的课

        # 将所有入度为0的节点（不需要先修课）入队，队列为当前可修的课程
        lst = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                lst.append(i)
        queue = deque(lst)
        # 拓扑排序：依次弹出当前可修(修完)的课程，并更新每个后继课程的入度表，寻找下一轮可修课程入队
        count = 0
        while queue:
            pre = queue.popleft() # 弹出修完的课程
            count += 1            # 记录修完的课程数量
            for cur in adjacency[pre]:  #找到这门课的所有后继课程
                indegrees[cur] -= 1 #所有后继课程的先修数量-1
                if indegrees[cur] == 0: #发现不需要先修课了则入队
                    queue.append(cur)

        return count == numCourses #如果修完课程=总数，说明不存在“环”