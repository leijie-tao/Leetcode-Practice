# 1. Need to know if there is a prerequisite -----> indegree
# 2. Need to know what's the next course  ------> adj
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        indegree = [0] * numCourses              # record how many prerequisites are needed
        adj = [[] for _ in range(numCourses)]    # find next eligible course
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        # Iterate all courses, add eligible courses into queue
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        # Deal with each course in order. (check if next course is eligible, and add it into queue)
        while q:
            c = q.popleft()
            res.append(c)
            for neighbor in adj[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if len(res) == numCourses:
            return res
        else:
            return []