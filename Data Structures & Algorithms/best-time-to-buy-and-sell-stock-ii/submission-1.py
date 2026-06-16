class Solution:
    def maxProfit(self, prices: List[int]):
        
        """
        [7, 1, 5, 3, 6, 4]
        compare next-next days
         i > i-1
         1) 1 7 
         2) 5 > 1 = 4 profit += (5-1)
         3) 3 > 5 
         4) 6 > 3 = 3 profit += (6-3)  
         5) 4 > 6
        """

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit

    