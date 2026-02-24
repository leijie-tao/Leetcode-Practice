class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]: #后面的值大于前面的值，则立刻卖掉
                profit += prices[i] - prices[i-1]

        return profit