class Solution:
    def rob(self, nums: list[int]) -> int:

        # Edge Case: No houses to rob
        if not nums:
            return 0
        
        # Edge Case: Only one house exists
        # (We handle this separately because our slice logic requires at least 2 houses)
        if len(nums) == 1:
            return nums[0]

        # Circular Logic: You can't rob both the first and last house.
        # We solve two linear versions of the problem:
        # 1. All houses EXCEPT the last one.
        # 2. All houses EXCEPT the first one.
        case_exclude_last = self.rob_linear_range(nums[:-1])
        case_exclude_first = self.rob_linear_range(nums[1:])

        return max(case_exclude_last, case_exclude_first)

    def rob_linear_range(self, house_values: list[int]) -> int:
        """Standard House Robber logic for a straight line of houses."""
        # rob_prev_1: Max profit including/excluding the immediate previous house
        # rob_prev_2: Max profit from two houses ago
        rob_prev_1 = 0 
        rob_prev_2 = 0
        
        for current_loot in house_values:
            # Decision: 
            # Option A: Rob current house + profit from 2 houses ago
            # Option B: Skip current house and keep profit from 1 house ago
            current_max = max(current_loot + rob_prev_2, rob_prev_1)
            
            # Slide the window forward
            rob_prev_2 = rob_prev_1
            rob_prev_1 = current_max
            
        return rob_prev_1    

        # recursive appraoch 

        # def rob_linear_range(self, nums: list[int]) -> int:
        # # Create a memory array of the same length as nums, filled with None
        # memo = [None] * len(nums)
        
        # def dp(i: int) -> int:
        #     # Base case: We have walked past the last house
        #     if i >= len(nums):
        #         return 0
            
        #     # MEMORY CHECK: If we already calculated this, return the saved answer!
        #     if memo[i] is not None:
        #         return memo[i]
            
        #     # Decision 1: Rob current house, then jump to house i + 2
        #     rob_this = nums[i] + dp(i + 2)
            
        #     # Decision 2: Skip current house, check the very next house i + 1
        #     skip_this = dp(i + 1)
            
        #     # SAVE TO MEMORY: Store the best result before returning it
        #     memo[i] = max(rob_this, skip_this)
            
        #     return memo[i]

        # # Start our decision tree at the first house (index 0)
        # return dp(0)
    # # also see https://leetcode.com/problems/house-robber/description/