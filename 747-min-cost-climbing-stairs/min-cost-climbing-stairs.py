class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        #1. dp[i]: min cost to reach i   --->  return dp[n]
        n = len(cost)
        dp = [0] * (n + 1)

        #2. Base Case
        dp[0] = 0
        dp[1] = 0

        # 3. Update dp[i] in the iteration, using state transition equation.
        for i in range(2, n + 1):
            one_step = cost[i - 1] + dp[i - 1]
            two_step = cost[i - 2] + dp[i - 2]
            dp[i] = min(one_step, two_step)

        return dp[n]