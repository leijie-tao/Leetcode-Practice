class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp[i]:the minimum number of coins to get the amount
        #create dp and max values, and update the values with minimum numbers 
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:      #take each coin to try
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1) #compare previous dp[i] with current dp[i - coin] + 1

        #check if dp[amount] has been updated
        if dp[amount] != amount + 1:
            return dp[amount]  
        else:
            return -1