class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

    # That is a very common question, and understanding this "plus one" "(len(nums) + 1)" trick is the key to mastering the prefix sum pattern.
    #The main reason we make the prefix array one element larger than the input array is to cleanly handle edge cases and avoid out-of-bounds errors without writing extra if/else statements.

    #If you look at the core formula in the range_sum(), you'll notice it relies on this offset. To get the sum of everything up to index i, we need to subtract the sum of everything before our starting point. If our starting point is index 0, we have to subtract prefix[0]
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        for idx, num in enumerate(nums): # T: O(n), S: O(n)
            prefix_sum[idx + 1] = prefix_sum[idx] + num

        # the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
        for idx, num in enumerate(nums):
            left = prefix_sum[idx] # everything strictly to the left of i
            right = prefix_sum[n] - prefix_sum[idx + 1]

            if left == right:
                return idx

        return -1
