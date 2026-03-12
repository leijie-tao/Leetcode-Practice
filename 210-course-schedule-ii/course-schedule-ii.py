class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #创建入度表（记录cur的先修数量）、邻接表（记录pre后续课程）
        indegree = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]
        for  cur, pre in prerequisites:
            indegree[cur] += 1
            adjacency[pre].append(cur)

        #构建队列，可修课程依次入队
        lst = []
        for i in range(numCourses):
            if indegree[i] == 0:
                lst.append(i)
        queue = deque(lst)

        #bfs拓扑排序，弹出已修课程添加至result。遍历邻接表中当前pre的后续课程列表，更新入度，发现0入度再次入队
        result = []
        while queue:
            pre = queue.popleft()
            result.append(pre)
            for cur in adjacency[pre]:
                indegree[cur] -= 1
                if indegree[cur] == 0:
                    queue.append(cur)
        
        #检查是否存在环（课程修完）
        if len(result) == numCourses:
            return result
        else:
            return []
