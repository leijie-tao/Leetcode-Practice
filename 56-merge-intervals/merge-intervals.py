class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        # save each non-overlapping interval
        res = [intervals[0]]

        # loop through the list, and check if each interval overlaps with previous one
        for interval in intervals:
            # if overlap, update the range of last element
            if interval[0] <= res[-1][1]:
                res[-1][0] = min(interval[0], res[-1][0])
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)

        return res
                