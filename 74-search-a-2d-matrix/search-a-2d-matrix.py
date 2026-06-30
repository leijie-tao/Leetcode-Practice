class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # brute force
        # m = len(matrix)
        # n = len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == target:
        #             return True
        # return False


        #Binary Search
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            #Key part: calculate the coordinate.
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False