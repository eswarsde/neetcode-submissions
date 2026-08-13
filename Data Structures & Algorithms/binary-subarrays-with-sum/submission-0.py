class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # # 1. BASE CASE: The "invisible zero" prefix before the array starts
        prev_seen_sum_count = defaultdict(int)
        prev_seen_sum_count[0] = 1

        total_num_subbary_sum = 0

        running_sum = 0

        for num in nums:
            running_sum += num
            target_to_chop = running_sum - goal

            # 2. THE TALLY: If we've seen the prefix we need to chop off, add its count
            total_num_subbary_sum += prev_seen_sum_count[target_to_chop]

            prev_seen_sum_count[running_sum] +=1

        

        return total_num_subbary_sum


        