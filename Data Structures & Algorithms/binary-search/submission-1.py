class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n -1
        
        while left <= right:
            mid = (left + right)//2
            curr_val = nums[mid]

            if curr_val == target:
                return mid
            elif curr_val < target:
                left = mid + 1
            else:
                right = mid -1 

        return -1