class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxWater = 0                                        #Maintain a max value
        while left < right:
            current = min(height[left], height[right]) * (right - left)     #The area = shorter height * width
            if current > maxWater:                          #Update maxWater. Or use max(maxWater, curernt)
                maxWater = current
            if height[left] >= height[right]:               #Move the shorter height
                right -= 1
            else:
                left += 1
        return maxWater
            
