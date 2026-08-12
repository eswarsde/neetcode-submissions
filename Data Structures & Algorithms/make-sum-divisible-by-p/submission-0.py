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