class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # sorted
        # distinct
        left, right = 0, len(nums) - 1

        # Keep searching while there is still a valid range [left, right].
        # We shrink the range until left becomes the insertion position.
        while left <= right:
            mid = left + (right - left) // 2

            # If nums[mid] is too small, the insertion position must be
            # strictly to the right of mid.
            if nums[mid] < target:
                left = mid + 1
            else:
                # nums[mid] >= target means mid could be the answer,
                # so keep searching on the left side for the first such index.
                right = mid - 1

        # left is now the first index where target can be inserted.
        # This also correctly returns len(nums) if target is larger than all values.
        return left
        