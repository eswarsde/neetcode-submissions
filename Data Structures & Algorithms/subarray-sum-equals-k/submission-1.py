from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        We keep a hashmap of previously seen sum frequencies. At each element, we compute 
        target_to_chop = running_sum - k to see how many earlier running sums 
        would make the current subarray sum to exactly k.
        """

        # ==============================================
        # PREFIX SUM + HASHMAP THINKING TEMPLATE
        # ==============================================

        # 0) QUESTION AT THE CURRENT INDEX:
        # How many subarrays ENDING at the current index
        # have a sum equal to k?

        # 1) WHAT INFORMATION DO I NEED FROM THE PAST?
        # prev_sum_counts[sum] = 
        # how many times this running sum has appeared before.
        prev_sum_counts = defaultdict(int)

        # Base case:
        # A running sum of 0 exists once before the array starts.
        #
        # This allows us to count subarrays that begin at index 0.
        #
        # Example:
        # nums = [2], k = 2
        # running_sum = 2
        # target_to_chop = 2 - 2 = 0
        # prev_sum_counts[0] must already be 1.
        prev_sum_counts[0] = 1

        # 2) STATE CARRIED FROM LEFT TO RIGHT:
        # Sum of all numbers processed so far.
        running_sum = 0

        # Final number of valid subarrays.
        total_count = 0

        for num in nums:

            # 3) INCLUDE THE CURRENT NUMBER
            # running_sum is now the total sum ending here.
            running_sum += num

            # We want:
            # running_sum - previous_sum = k
            #
            # Therefore, the previous sum we need to chop off is:
            target_to_chop = running_sum - k

            # Every previous occurrence of target_to_chop creates
            # one valid subarray ending at the current position.
            total_count += prev_sum_counts[target_to_chop]

            # Record the current running sum for future indices.
            #
            # IMPORTANT:
            # Check for valid subarrays BEFORE recording running_sum.
            # Otherwise, when k == 0, we could incorrectly count
            # an empty subarray using the current sum against itself.
            prev_sum_counts[running_sum] += 1

        return total_count