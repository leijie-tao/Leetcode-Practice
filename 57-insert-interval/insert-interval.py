# -------------------- O(n): For a sorted list, check the relationship between elements and newInterval. (on left side, overlap, and on the right side) ----------------
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         res = []
#         n = len(intervals)
#         i = 0
#         # Interval is on the left side of nweInterval without overlaping
#         while i < n and intervals[i][1] < newInterval[0]:
#             res.append(intervals[i])
#             i += 1
#         # Interval overlaps with newInterval, and need to update the ends or merge intervals by using newIntervals
#         while i < n and intervals[i][0] <= newInterval[1]:
#             newInterval[0] = min(newInterval[0], intervals[i][0])
#             newInterval[1] = max(newInterval[1], intervals[i][1])
#             i += 1
#         res.append(newInterval)
#         # Interval is on the right side of nweInterval without overlaping
#         while i < n and intervals[i][0] > newInterval[1]:
#             res.append(intervals[i])
#             i += 1
        
#         return res


# -------------------- O(nlog n): based on 56. Merge Interval -------------------
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for cur in intervals:
            if cur[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], cur[1])
            else:
                res.append(cur)
        return res