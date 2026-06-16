class Solution:
    # tracking the states each day
    """
    3 possible stateus on a given end of the day 
    1) HOLD: You currently hold exactly one coin.
    How you get here:
        i) bought today, REST yesterday 
        ii) holding from yesterday 
    2) SOLD: You just sold your coin today
    How you get here:
        i) Sold today, this means HOLD yesterday 
    3) REST: You don't hold a coin, and you didn't just sell one.
    How you get here:
        i) forced rest(cooldown) -> SOLD yesterday, cooldown today 
        ii) you decided do nothing today, kept resting
    """
    def maxProfit(self, prices: List[int]) -> int:
         # day 0
        HOLD = -prices[0]
        SOLD = 0
        REST = 0

        for i in range(1, len(prices)):
            todays_price = prices[i]

            prev_HOLD = HOLD
            prev_SOLD = SOLD
            prev_REST = REST
    

            HOLD = max(prev_HOLD, (prev_REST - todays_price))
            SOLD = prev_HOLD + todays_price
            REST = max(prev_REST, prev_SOLD)

        # Last day no buy
        return max(SOLD, REST)
