class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [1,1,2,3,4]
        #    w r

        if len(nums) == 1:
            return 1
        
        write = 1

        for read in range(1, len(nums)):
            if nums[read] != nums[read -1]:
                nums[write] = nums[read]
                write+=1

        return write
            

        # write = 1 #If the array is not empty, the first element (index = 0) is always unique.
        # for read in range(1, len(nums)):
        #     if nums[read]!=nums[write-1]: # the value at read pointer is a new unique value
        #         nums[write] = nums[read]
        #         write+=1
                
        # return write

        