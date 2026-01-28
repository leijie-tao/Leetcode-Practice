class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        nums = range(1, n+1)
        def backtrack(start):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return res
