class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # # Naive
        # for i in range(len(nums)):
        #     nums[i] *= nums[i]
        # nums.sort()
        # return nums

        # # Time complexity: O(nlogn)
        # # Space complexity: O(n) depending on the sorting algorithm.

        # approach 2

        # Key observation
        # The array is sorted in non-decreasing order.
        # The values with the largest magnitude are at the ends:
        # far left may be a large negative number
        # far right may be a large positive number
        # After squaring, the largest square must come from one of those two ends.


        # Core idea
        #     Keep two pointers:
        #     left at the start
        #     right at the end
        #     Also keep a write position write at the end of the output array.
        #     On each step:
        #     compare abs(nums[left]) and abs(nums[right])
        #     put the larger square into ans[write]
        #     move the matching pointer inward
        #     move write one step left


        n = len(nums)

        # Preallocate the answer so we can fill it from right to left.
        ans = [0] * n

        # left/right scan the remaining candidates.
        # write marks the next largest position to fill in the output.
        left = 0
        right = n - 1
        write = n - 1

        # Continue while there are still values to place.
        # Stopping rule: once left passes right, every input value has been used.
        while left <= right:
            left_abs = abs(nums[left])
            right_abs = abs(nums[right])

            # The larger absolute value produces the larger square,
            # so it belongs at the current back position of the answer.
            if left_abs > right_abs:
                ans[write] = left_abs * left_abs
                left += 1
            else:
                ans[write] = right_abs * right_abs
                right -= 1

            # Move left in the answer because we just filled one position.
            write -= 1

        return ans