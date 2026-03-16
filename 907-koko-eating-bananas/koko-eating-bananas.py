class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #速度为k：每次最少吃1个，最多吃max(piles)个 ——> 求刚好满足要求的目标速度
        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right - left)//2
            total_hours = 0
            #遍历累加计算每堆需要的时间，math.ceil()向上取整
            for p in piles:
                total_hours += math.ceil(p / mid)
            #total_hours小于则排除较快的速度，大于排除较慢的速度
            if total_hours <= h:
                right = mid -1
            else:
                left = mid + 1

        return left