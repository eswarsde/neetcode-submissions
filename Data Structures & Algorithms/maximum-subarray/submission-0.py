class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize both current_sum and best_sum to the first element
        current_sum = nums[0]  # current_sum is the best subarray sum ending at the current index
        best_sum = nums[0]     # best_sum is the best subarray sum seen overall so far

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            value = nums[i]  # value is the current element we are processing

            # Decide whether to start a new subarray at this element or extend the previous one
            current_sum = max(value, current_sum + value)  # best subarray ending at i

            # Update the global best if the current ending subarray is better
            if current_sum > best_sum:
                best_sum = current_sum  # store the new maximum subarray sum found so far

        # After processing all elements, best_sum holds the maximum subarray sum
        return best_sum  # return the final answer
            