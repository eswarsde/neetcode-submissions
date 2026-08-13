class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        # If you want a subarray to have an odd sum, you have to think about how addition and subtraction work with even and odd numbers.

        # Remember our golden rule: Subarray = Current Prefix - Past Prefix.
        # To get an odd result from subtraction, the two numbers must be opposites:
        #  1. ODD - EVEN = ODD (e.g., 7 - 2 = 5)
        #  2. EVEN - ODD = ODD (e.g., 8 - 3 = 5)
        #   If you subtract two evens (8 - 2 = 6) or two odds (7 - 3 = 4), you always get an even number, which we don't want.

        prev_seen_subarray_count = {0: 1, 1: 0} # 0 is even, 1 is odd 
        running_sum = 0
        total_subarrays_with_odd_sum = 0

        for num in arr:
            running_sum += num

            # 1. Get current parity (0 for even, 1 for odd)
            current_parity = running_sum % 2

            # 2. We want to chop off the OPPOSITE parity to leave an odd sum behind
            target_to_chop = 1 - current_parity

            # 3. Add however many opposite-parity prefixes we've seen to our total
            total_subarrays_with_odd_sum += prev_seen_subarray_count[target_to_chop]

            # 4. Update the ledger with our current parity
            prev_seen_subarray_count[current_parity] += 1


        return total_subarrays_with_odd_sum





        