class Solution:
    # Control the boundary
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        # Use 4 boundaries to constraint the route.
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        res = []

        # Keep shrinking when there is still an inner space
        while top <= bottom and left <= right:
            # Go right: "while" confirms there are available rows
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            
            # Go down: "while" confirms there are available colums
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # Go left: After changing top boundaries, check if there are still available rows
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # Go up: After changing right boundaries, check if there are still available colums
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        
        return res
