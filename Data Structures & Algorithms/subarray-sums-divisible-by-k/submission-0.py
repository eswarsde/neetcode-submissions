class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        # (PrefixRight - PrefixLeft) % k == 0
        # If you rearrange that algebra, you get this golden rule: 
        #   PrefixRight % k == PrefixLeft % k

        # This means if your current "running_sum" % k is 3, and you have seen a previous prefix sum that also had a remainder of 3, the chunk of numbers between them must be perfectly divisible by k!

        # Instead of asking the dictionary, "Have I seen running_sum - k?", you just ask, "Have I seen my current remainder before?"

        total_subarrays_div_by_k = 0

        prev_seen_remainder_count = defaultdict(int)
        prev_seen_remainder_count[0] = 1


        running_sum =  0

        for num in nums:

            running_sum += num

            remainder = running_sum % k

            # 3. Ask the dictionary: Have we seen this exact remainder in the past?
            # If yes, chopping those past prefixes off leaves a subarray divisible by k.
            total_subarrays_div_by_k += prev_seen_remainder_count[remainder]

            prev_seen_remainder_count[remainder] += 1





        return total_subarrays_div_by_k
        