class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left_pointer = 1 #If the array is not empty, the first element (index = 0) is always unique.
        for right_pointer in range(1, len(nums)):
            if nums[right_pointer]!=nums[right_pointer-1]: # is the value at right_pointer is a new unique value
                nums[left_pointer] = nums[right_pointer]
                left_pointer+=1
                
        return left_pointer

        