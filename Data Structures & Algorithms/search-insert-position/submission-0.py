class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # hint of binary search is that input is sorted, 

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # If the loop finishes, 'left' is the insertion index
        # because last when we checked "nums[mid] < target", we increased +1
        return left


        