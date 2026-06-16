
from typing import List  # Import List for type hints
import math 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # If the amount is 0, no coins are needed
        if amount == 0:
            return 0  # trivial case
        
        INF = math.inf  # A large number to represent "impossible"
        
        # Memoization dictionary: maps remaining amount to minimal coins needed
        memo = {}  # type: dict[int, int]
        
        def dfs(rem: int) -> int:
            """
            Return the minimum number of coins needed to form 'rem'.
            If it is not possible, return INF.
            """
            # Base case: exact amount reached
            if rem == 0:
                return 0  # no more coins needed
            
            # Base case: overshoot, invalid path
            if rem < 0:
                return INF  # impossible to form this negative amount
            
            # If we have already computed this state, reuse it
            if rem in memo:
                return memo[rem]  # return cached result
            
            # Otherwise, compute the result from scratch
            best = INF  # start with "impossible"
            
            # Try using each coin and take the best result
            for coin in coins:
                # Use one coin of this denomination and solve for the remainder
                sub = dfs(rem - coin)  # recursive call for rem - coin
                
                # If sub is not INF, update best (sub + 1 counts this coin)
                if sub + 1 < best:
                    best = sub + 1
            
            # Store the computed best result in the memo dictionary
            memo[rem] = best
            
            # Return the best result for this remaining amount
            return best
        
        # Start the recursion from the full amount
        result = dfs(amount)
        
        # If the result is still INF, no combination of coins can form 'amount'
        if result >= INF:
            return -1  # impossible case
        
        # Otherwise, return the minimum number of coins found
        return result
