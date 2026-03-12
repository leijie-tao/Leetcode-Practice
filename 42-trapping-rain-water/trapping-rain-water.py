class Solution:
    def trap(self, height: List[int]) -> int:
        #核心：每单位能接水 min(left_max, right_max) - height
        if not height:
            return 0

        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        result = 0
        while left < right:
            #若min短板在左侧，更新左侧最大值left_max，累加单位水量，移动左指针
            if height[left] <= height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
                left += 1
            #若min短板在右侧，更新右侧最大值right_max，累加单位水量，移动右指针
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
                right -= 1

        return result
