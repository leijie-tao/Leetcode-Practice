class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        count = 0
        for cur in intervals[1:]:
            if cur[0] < res[-1][1]:
                count += 1
                # update res[-1], and keep smaller end to get minimum removal
                res[-1] = min(res[-1], cur, key=lambda x: x[1])
            else:
                res.append(cur)
        return count