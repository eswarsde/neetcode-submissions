class Solution:
    def maxProfit(self, prices: List[int]):
        if len(prices) < 2:
            return 0
        min_price_so_far = float('inf')
        max_profit_so_far = 0

        for price in prices:
            # keep track of min_price 
            if price < min_price_so_far:
                min_price_so_far = price

            elif max_profit_so_far < (price - min_price_so_far):
                max_profit_so_far = price - min_price_so_far

        return max_profit_so_far


        
        