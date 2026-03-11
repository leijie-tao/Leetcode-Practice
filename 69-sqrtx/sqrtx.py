class Solution:
    def mySqrt(self, x: int) -> int:
        #binary search:在[0，x]区间找整数k，k^2 <= x and (k+1)^2 >=x
        if x < 2:
            return x
        left, right = 0, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == x:     #找到开根整数
                return mid
            elif square < x:    #更新下界
                left = mid + 1
            else:
                right = mid - 1 #更新上界

        return right    #stop condition: left > right. The result is in [right,left], so right is the integer of the down side.