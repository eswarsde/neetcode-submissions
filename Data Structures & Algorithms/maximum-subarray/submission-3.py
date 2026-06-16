class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize both current_sum and best_sum to the first element
        current_sum = 0  # current_sum is the best subarray sum ending at the current index
        best_sum = nums[0]     # best_sum is the best subarray sum seen overall so far

        # Iterate through the array starting from the second element
        for num in nums:
           
            # Decide whether to start a new subarray at this element or extend the previous one
            # watch - https://neetcode.io/courses/advanced-algorithms/0
            current_sum = max(current_sum, 0) # if existing curr_sum was negative, it adds no value to add the next num to it
                                              # bcoz a negative number is only bring the value down, but we are tragetting for max
            current_sum = current_sum + num

            # Update the global best if the current ending subarray is better
            # store the new maximum subarray sum found so far
            best_sum = max(best_sum, current_sum)

        # After processing all elements, best_sum holds the maximum subarray sum
        return best_sum  # return the final answer
            