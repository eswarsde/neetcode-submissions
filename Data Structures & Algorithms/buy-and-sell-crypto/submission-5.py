class Solution:
    def maxProfit(self, prices: List[int]):
        if len(prices) < 2:
            return 0



        ########################################################
        # Input: prices = [10,1,5,6,7,1]
        # Output: 6

        # Input: prices = [10,8,7,5,2]
        # Output: 0

        # Approach 1: Brute force         # o(n2) - time, o(1) - space
        # max_profit = 0

        # for buy in range(0, len(prices)-1):
        #     for sell in range(buy+1, len(prices)):
        #         profit = prices[sell] - prices[buy]
        #         if profit > max_profit:
        #             max_profit = profit
        
        # return max_profit


        # Cheapest price seen so far

        min_price_so_far = prices[0]
        max_profit_so_far = 0

        for price in prices[1:]:
            # sell - buy
            profit = price - min_price_so_far

            if profit > max_profit_so_far:
                max_profit_so_far = profit
            if price < min_price_so_far:
                min_price_so_far = price

        
        return max_profit_so_far























































        # # 2 pointers

        # left, right = 0, len(prices) - 1

        # max_profit = 0

        # while left < right:
        #     profit = prices[left] - prices[right]
        #     if profit > max_profit:
        #         max_profit = profit

            



        # return max_profit















        # min_price_so_far = float('inf')
        # max_profit_so_far = 0

        # for price in prices:
        #     # Check if we found a new, lower price to buy at
        #     if price < min_price_so_far:
        #         min_price_so_far = price

        #     # Otherwise, check if selling today yields a better profit
        #     elif max_profit_so_far < (price - min_price_so_far):
        #         max_profit_so_far = price - min_price_so_far

        # return max_profit_so_far


        
        