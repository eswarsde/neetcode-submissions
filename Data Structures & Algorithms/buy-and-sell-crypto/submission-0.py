class Solution:
    def maxProfit(self, prices: List[int]):
        if len(prices) < 2:
            return 0
        min_price_so_far = float('inf')
        max_profit = 0

        for price in prices:
    
            if price < min_price_so_far:
                min_price_so_far = price

            elif price - min_price_so_far > max_profit:
                max_profit = price - min_price_so_far

        return max_profit


        
        