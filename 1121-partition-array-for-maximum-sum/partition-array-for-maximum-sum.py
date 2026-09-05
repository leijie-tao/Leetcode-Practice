class Solution:
    # "求最值/计数" + "答案由多步决策拼成"，指数级暴力枚举 → DP
    # 当前决策会"影响后续的选择空间" → DP            决策之间不互相影响 → 贪心
    # 定义子问题 dp[i]/dp[i][j]的含义
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)  # dp[i] means "the max sum of partition array" by index i
        dp[0] = 0  

        # Record dp[i], and i is from 1 to n ————> i is the end of a window
        for i in range(1, n + 1):
            cur_max = 0
            # j is the length of the window, moving from i to the left side
            for j in range(1, k + 1):
                if i - j < 0:              # left end is arr[0]
                    break
                # keep updating the max value in the window and dp[i]
                cur_max = max(cur_max, arr[i - j]) 
                dp[i] = max(dp[i], dp[i - j] + j * cur_max)

        return dp[n]