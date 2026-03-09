class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1  #两段向中间的双指针
        max_amount = 0
        while l < r:
            curr_amount = min(height[l], height[r]) * (r - l)   #容量 = 短板 * 指针距离
            max_amount = max(max_amount, curr_amount)
            if height[r] < height[l]:   #移动短板
                r -= 1
            else:
                l += 1
        return max_amount
