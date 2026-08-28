class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the list by start value to make mergeable elements adjacent
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for cur in intervals[1:]:
            # use the last element of res to show the latest merged result （intervals[i] and [i+1] can't show consistently merging)
            if res[-1][1] >= cur[0]:
                res[-1][1] = max(cur[1], res[-1][1])
            # if there is no overlaping, add the element directly
            else:
                res.append(cur)
       
        return res