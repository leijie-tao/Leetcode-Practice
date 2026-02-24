class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if p < buy_price: #小于买入价则更新买入价
                buy_price = p
            else: #大于买入价则更新profit
                profit = max(profit, p - buy_price)
        
        return profit