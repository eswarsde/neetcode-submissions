class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1 #If the array is not empty, the first element (index = 0) is always unique.
        for read in range(1, len(nums)):
            if nums[read]!=nums[write-1]: # is the value at right_pointer is a new unique value
                nums[write] = nums[read]
                write+=1
                
        return write

        