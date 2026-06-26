class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Maintain two vaiables and update them during iteration
        minprice = float('inf')
        maxprofit = 0
        for p in prices:
            minprice = min(minprice, p)                 # buy at minprice
            maxprofit = max(maxprofit, p - minprice)    # p is always after current minprice
        return maxprofit