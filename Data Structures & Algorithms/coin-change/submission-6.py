class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # 1. Bottom up approach
        # start at zero and build your way up to the target amount

        # Use amount + 1 as an impossible sentinel or use infinity
        dp = [amount + 1] * (amount + 1) # 0, 1... amount
        # base case
        dp[0] = 0

        for amt in range(1, amount + 1): # calculating all the way unttil anount
            for coin in coins:
                if amt - coin >= 0: # this coin is useable 
                    # 1  is for the coin we used
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])

        return dp[amount] if dp[amount] != (amount + 1) else - 1

        # # 2. Top Down approach 
        # # start at amount and build your way up to zero 
        # # How to model this problem 
        # # Say we start with some coin and then we know the remaining amount -> now you have the option to pick any denomiation <= remaining balance
        # # also there might sub problems we solve again and again # say remaining balance is 5, we could memoize the number of coins needed to make 5 to zero
        #   # subproblem: Minimum coins needed to make this amount
      

        # # Edge case: making amount 0 needs 0 coins.
        # if amount == 0:
        #     return 0

        # # Use amount + 1 as an impossible sentinel.
        # # A valid answer can never need more than `amount` coins if coin 1 exists,
        # # so amount + 1 safely acts like infinity for "minimum coins" comparisons.
        # impossible = amount + 1

        # # Memo maps `remaining amount` -> `minimum coins needed from here`.
        # # Memoization avoids repeated work because many recursion paths
        # # ask for the same remaining amount again and again.
        # memo: dict[int, int] = {}

        # def dfs(remaining: int) -> int:
        #     # DFS state meaning:
        #     # Return the minimum number of coins needed to make exactly `remaining`.
        #     # If impossible, return the sentinel `impossible`.

        #     # Base case: exact amount formed, so no more coins are needed.
        #     if remaining == 0:
        #         return 0

        #     # Base case: overshot below 0, so this path is invalid.
        #     if remaining < 0:
        #         return impossible

        #     # If we already solved this remaining amount, reuse it immediately.
        #     if remaining in memo:
        #         return memo[remaining]

        #     # Current work for this state:
        #     # try each coin as the next choice and keep the smallest valid answer.
        #     best = impossible

        #     # Choices / neighbors:
        #     # each coin leads to the next state `remaining - coin`.
        #     for coin in coins:
        #         new_remaining_amount = remaining - coin
        #         if new_remaining_amount >= 0:
        #             cadidate_result = dfs(new_remaining_amount)
        #             best = min(best, cadidate_result + 1)

        #     # Store the answer for this state before returning it.
        #     memo[remaining] = best
        #     return best

        # minCoins = dfs(amount)

        # # If the final state is still impossible, return -1 as required.
        # return -1 if minCoins == impossible else minCoins

