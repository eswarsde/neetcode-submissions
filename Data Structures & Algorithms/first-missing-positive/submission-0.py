class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Here is the full implementation of the "Rightful Home" (Cyclic Sort) strategy.
        # Imagine each index i in the array is a "home" for a specific number.
         # Index 0 is the home for the number 1.
         # Index 1 is the home for the number 2.
         # Index i is the home for the number i + 1.

        n = len(nums)
        
        # Phase 1: The Sorting (Putting numbers in their rightful homes)
        for i in range(n):
            # While the current number is valid (1 to n) 
            # AND it's not already at its correct index...
            # AND it's not a duplicate of what's already at the target index
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap it to its target index
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        # Phase 2: The Inspection
        # Look for the first index that doesn't hold the correct number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Phase 3: The Edge Case
        # If the array was perfectly filled [1, 2, ..., n], 
        # then the missing one is n + 1
        return n + 1        