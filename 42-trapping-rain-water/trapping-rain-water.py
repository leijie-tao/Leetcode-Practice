class Solution:
    def trap(self, height: List[int]) -> int:
        # # brute force: calculate trapped water of each position
        # n = len(height)
        # res = 0
        # #trapped water = min(maxHeightOnTheLeft, maxHeightOnTheRight) - currentHeight
        # for i in range(n):
        #     left_max = max(height[:i+1])    
        #     right_max = max(height[i:])   
        #     res += min(left_max, right_max) - height[i]
        # return res
        
        
        
        #Two pointers: Use left/right pointer to loop through. Maintain max vairable to determain the trapped water.
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        res = 0
        
        while left < right:
            # For the whole container, the water is determined by the shorter side.
            if height[left] <= height[right]:
                # For each position, the difference height is determined by the max height on this side.
                left_max = max(left_max, height[left])
                res += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                res += right_max - height[right]
                right -= 1

        return res

