class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = float("inf")
        for i in range(0,n):
            if min_price > prices[i]:
                min_price = prices[i]
            if max_profit < prices[i] - min_price:
                max_profit = prices[i] - min_price

        return max_profit
