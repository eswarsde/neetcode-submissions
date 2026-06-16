class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0 
        right = len(nums) -1

        # We use < instead of <= because we are narrowing
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # In a perfectly sorted array (no rotation), the middle is always smaller than the right end.
                  # If we see nums[mid] > nums[right], then that means we are standing on the higher staircase, 
                  # but the array has already "dropped" to the lower staircase further to the right.
                # The minimum must be in the right half.
                # Since nums[mid] is greater than nums[right], 
                # mid cannot be the minimum.
                left = mid + 1
            else:
                # nums[mid] <= nums[right]
                # the sequence from mid to right looks like a normal, upward-climbing staircase.
                # This means the "drop" happened somewhere at or before mid
                # The minimum is in the left half or is mid itself.
                # We keep mid as a possibility.
                right = mid

        # After the loop, left == right, pointing to the minimum.
        return nums[left]

            


        