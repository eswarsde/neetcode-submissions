class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        prev_seen_remainder_index = {0: -1}
        running_sum = 0

        for idx, num in enumerate(nums):
            running_sum += num
            # the sum of the elements of the subarray is a multiple of k
            # its length is at least two
            target_to_chop = running_sum % k

            if target_to_chop in prev_seen_remainder_index:
                # get that subarray and check length ??
                prev_index = prev_seen_remainder_index[target_to_chop]
                if idx - prev_index >= 2:
                    return True
            else:
                prev_seen_remainder_index[target_to_chop] = idx

        return False



        
        