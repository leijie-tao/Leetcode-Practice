class Solution:
    def climbStairs(self, n: int) -> int:
        #Special case handling
        if n <= 1:
            return n
        #Record index 0 to n
        dp = [0] * (n + 1)  
        #Base case
        dp[1] = 1
        dp[2] = 2
        #Iteration & State Transition Equation
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

