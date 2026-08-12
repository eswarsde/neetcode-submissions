from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # The sum of any subarray can be found by taking the total sum up to the end of the chunk, and subtracting the sum of the elements before the chunk starts.
        # SubarraySum = PrefixRight - PrefixLeft

        # Since the problem asks us to find subarrays that equal exactly k, we plug k into the equation:
        # k = PrefixRight - PrefixLeft


        # what I don't understand is, Say I have seen "4" 4 different times, how is that they are contigious subarrays ?? they array could be broken in between
                # This is the absolute most common mental roadblock for this pattern, so I'm really glad you asked. It feels like magic, but it’s actually just pure geometry.

                # The secret lies in the definition of a "prefix sum."

                # By definition, a prefix sum is **never broken**. It is a solid, contiguous block of numbers starting from index `0` and stretching perfectly to whatever index you were at.

                # When you ask the hashmap, *"Have I seen a `4` in the past?"*, you are actually asking: *"Are there any solid blocks starting from index 0 that add up to 4?"*

                # If the hashmap says, *"Yes, I have seen a `4` three different times,"* it means there are three **different indices** where a solid block from `0` added up to `4`.

                # ### Visualizing the Subtraction

                # Let's say your target is **`k = 3`**.
                # You are at index 5, and your current `running_sum` is **`7`**.
                # This means the solid block from index `0` to index `5` equals `7`.

                # To get a subarray of exactly `3`, you need to "chop off" a prefix of `4` from the beginning.

                # Let's look at an array that hits a prefix sum of `4` three different times because of negative numbers:
                # `nums = [4, -1, 1, -1, 1, 3]`

                # As we iterate, here is our `running_sum` at each step:

                # * Index 0: `[4]` ➔ **4** *(First time seeing 4)*
                # * Index 1: `[4, -1]` ➔ 3
                # * Index 2: `[4, -1, 1]` ➔ **4** *(Second time seeing 4)*
                # * Index 3: `[4, -1, 1, -1]` ➔ 3
                # * Index 4: `[4, -1, 1, -1, 1]` ➔ **4** *(Third time seeing 4)*
                # * **Index 5: `[4, -1, 1, -1, 1, 3]` ➔ 7**

                # Now you are at Index 5. Your `running_sum` is `7`. You need to chop off a prefix of `4`.
                # Your `prev_seen_sum_count` dictionary says you have seen `4` exactly **three times**.

                # Here is why they are all contiguous subarrays. Because your current finger is fixed at Index 5, you can make three different cuts based on those past prefix sums:

                # 1. **Cut 1 (at Index 0):** Chop off `[4]`.
                # What is left? The contiguous chunk `[-1, 1, -1, 1, 3]`. (Sum = 3)
                # 2. **Cut 2 (at Index 2):** Chop off `[4, -1, 1]`.
                # What is left? The contiguous chunk `[-1, 1, 3]`. (Sum = 3)
                # 3. **Cut 3 (at Index 4):** Chop off `[4, -1, 1, -1, 1]`.
                # What is left? The contiguous chunk `[3]`. (Sum = 3)

                # ### The Takeaway

                # You aren't piecing together broken parts of the array. The hashmap isn't storing disjointed elements.

                # The hashmap is just keeping track of **how many valid starting lines** you can draw behind you. Because your current `running_sum` represents the finish line, every time you subtract a valid past prefix sum, you are left with a perfectly contiguous chunk between that starting line and your current finish line!

                # Does seeing the cuts visually clear up why the remaining pieces are always unbroken?


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
        prev_seen_sum_count = defaultdict(int)
        prev_seen_sum_count[0] = 1


            # Sum of all numbers processed so far.
        running_sum = 0

        # Final number of valid subarrays.
        total_subarray_count = 0


        for num in nums:

            running_sum += num

            target_to_chop = running_sum - k
            total_subarray_count += prev_seen_sum_count[target_to_chop]
            prev_seen_sum_count[running_sum] = prev_seen_sum_count[running_sum] + 1

        return total_subarray_count


        