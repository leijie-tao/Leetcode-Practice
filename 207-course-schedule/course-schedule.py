class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Record indegree & prerequisite courses
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adj[pre].append(crs)    # pre -> crs
            indegree[crs] += 1      # pre <- crs
        
        #initialize the queue, and add first eligible course into the queue
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)


        # Every time finish a course, iterate the adjacent table to update indegree, and add new eligible courses into queue
        finish = 0
        while q:
            c = q.popleft()
            finish += 1
            for neighbor in adj[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return finish == numCourses
