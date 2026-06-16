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

    # # also see https://leetcode.com/problems/house-robber/description/
    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]

    #     memo = [[-1] * 2 for _ in range(len(nums))]

    #     def dfs(i, flag):
    #         if i >= len(nums) or (flag and i == len(nums) - 1):
    #             return 0
    #         if memo[i][flag] != -1:
    #             return memo[i][flag]
    #         memo[i][flag] = max(dfs(i + 1, flag),
    #                         nums[i] + dfs(i + 2, flag or (i == 0)))
    #         return memo[i][flag]

    #     return max(dfs(0, True), dfs(1, False))