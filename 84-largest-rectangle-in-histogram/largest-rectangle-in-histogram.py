class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Use stack to record the ascending heights
        max_area = 0
        n = len(heights)
        stack = [] 
        for i in range(n):
            #If current height is lower than the last element of stack, pop the element and regard it as height to calculate. (keep poping until all the element)
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()] 
                if stack: # If stack has elements, expand the width. Left side—>stack[-1].  Right side—>i-1
                    w = i -1 - stack[-1]
                else: #If steck is empty, current popped one is the lowest. The index of last one can be the width that cover all the left heights.
                    w = i
                max_area = max(max_area, h * w)
            stack.append(i)
        
        # The left elements of stack are smaller than the first descending one.
        while stack:
            h = heights[stack.pop()]
            if stack:
                w = n - stack[-1] - 1 
            else:
                w = n
            max_area = max(max_area, h * w)

        return max_area