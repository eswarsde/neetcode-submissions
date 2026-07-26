class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Input: nums = [3,2,2,3], val = 3
        # Output: k = 2, nums = [2,2,_,_]
        # write pointer # where the next element should go
        # read pointer -> scans every element in the array 
        # if nums[read] ! = val, nums[write] = nums[read]
           # wrte+=1
        write = 0
        for read in range(0, len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write+=1
            
        return write


        # write = 0
        # for read in range(len(nums)):
        #     if nums[read] != val: # KEEP
        #         nums[write] = nums[read]
        #         write +=1
        # return write


        