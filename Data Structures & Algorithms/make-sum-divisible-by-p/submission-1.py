class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        # on top if my mind, I am thinking we need to store prefix sum and index ?? that way we know if we need to remove 4, we will know at what prefix we can remove and the index so we can caluclat length

        # Key observation: array is full positive numbers and they always grow, but the remainder will cycle. You will likely see the exact same remainder multiple times at different indices. 

        # If you see a remainder of 3 at index 2, and then you see a remainder of 3 again at index 5... which index do we want to keep stored in the dictionary to ensure you find the shortest possible subarray?, the latest, we want to keep the last seen position to minimize the distance between your current position (i) and the past position (j)
        
        # Step 1: Find the total extra weight we need to chop off
        target_remainder = sum(nums) % p

        if target_remainder == 0:
            return 0

        # Step 2: Base case. The "invisible zero" prefix is conceptually at index -1
        prev_seen_remainder_index = {0: -1}

        running_sum = 0
        min_length = len(nums)

        # Subarray = Current - Past
        # Subarray Remainder = Current Remainder - Past Remainder  
        # Since we know the subarray we want to remove must equal our target_remainder, the equation becomes:
        #   target_remainder = current_rem - Past Remainder   
        #   Past Remainder = current_rem - target_remainder
        for idx, num in enumerate(nums):
            running_sum +=num

            current_rem = running_sum % p

            target_to_chop = (current_rem - target_remainder) % p

            if target_to_chop in prev_seen_remainder_index:
                distance = idx - prev_seen_remainder_index[target_to_chop]
                min_length = min(min_length, distance)

            # Step 5: Always overwrite the dictionary with the LATEST index
            prev_seen_remainder_index[current_rem] = idx


        return min_length if min_length < len(nums) else -1





# Let's use real numbers (Example 1)
# Let's say p = 7.

# The whole array has a target_remainder = 4 (it's 4 over the limit).

# You are walking through the array, and your current_rem = 6.

# You need to chop off a chunk that leaves you with 4.
# Past Remainder = 6 - 4
# Past Remainder = 2

# So, you ask your dictionary: "Have I seen a prefix with a remainder of 2?" (Because chopping off a 2 from your current 6 will perfectly remove that extra weight of 4).



# 4. Why the extra % p at the end of "target_to_chop = (current_rem - target_remainder) % p"
# What happens if your current_rem is smaller than the target_remainder?

# Let's say p = 7.

# target_remainder = 4.

# Your current_rem = 1.

# If we use our formula:
# Past Remainder = 1 - 4 = -3

# You can't have a remainder of -3. But because remainders operate in a continuous circle (like a clock), being -3 steps backward is the exact same as being +4 steps forward on a 7-hour clock.

# By wrapping the whole equation in modulo p like this:
# target_to_chop = (1 - 4) % 7 

# Python automatically wraps that -3 around the circle and calculates 4. You then ask the dictionary: "Have I seen a prefix with a remainder of 4?" (Because chopping a 4 off a 1 wraps backward around the circle and perfectly removes the extra weight of 4!).




