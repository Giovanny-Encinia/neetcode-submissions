class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")

        for n in prices:
            min_price = min(min_price, n)
            current_profit = n - min_price
            max_profit = max(max_profit, current_profit)

        return max_profit
        
            