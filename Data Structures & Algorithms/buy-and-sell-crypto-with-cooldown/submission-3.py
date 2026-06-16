class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        3 possible states at the end of a given day:

        1) HOLD: You currently hold exactly one stock.
           How you get here:
             i) You bought today, so you were in REST yesterday
             ii) You were already holding from yesterday

        2) SOLD: You just sold your stock today.
           How you get here:
             i) You sell today, so you were in HOLD yesterday

        3) REST: You don't hold a stock, and you didn't just sell one.
           How you get here:
             i) Forced rest (cooldown): you were in SOLD yesterday
             ii) You do nothing today and remain in REST
        """

        # Day 0
        HOLD = -prices[0]  # Bought on day 0
        SOLD = 0           # Can't really sell on day 0
        REST = 0           # Starting state

        for i in range(1, len(prices)):
            todays_price = prices[i]

            # Store previous day's values before updating
            prev_HOLD = HOLD
            prev_SOLD = SOLD
            prev_REST = REST

            # Calculate current day's values using previous day's values
            HOLD = max(prev_HOLD, prev_REST - todays_price)
            SOLD = prev_HOLD + todays_price
            REST = max(prev_REST, prev_SOLD)

        # On the last day, you can't count HOLD as final profit
        return max(SOLD, REST)