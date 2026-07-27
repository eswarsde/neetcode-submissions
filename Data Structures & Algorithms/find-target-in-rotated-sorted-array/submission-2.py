class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        # nums = [3,4,5,6,1,2], target = 1
        # Output: 4

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[right]: 
                # means right side is rotated otherwise - nums[mid] <= nums[right] in a normal sorted array
                #  so the LEFT side is perfectly sorted
                # 1. Check if the target is within that sorted left range
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 # Target is in the left half
                else:
                    left = mid + 1 # Target must be in the right half

            else:
                # # The right side is perfectly sorted.
                # Step 2: Check if the target is within that sorted right range
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target is in the right half
                else:
                    right = mid - 1  # Target must be in the left half

        return -1 # Target was never found