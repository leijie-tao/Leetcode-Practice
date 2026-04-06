class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]    #dp[i][j] means the total number of unique paths from (0, 0) to (i, j)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] #(i, j) can be reached from the left side dp[i-1][j] and the upper side dp[i][j-1]

        return dp[m-1][n-1]