class Solution:
    def moveZeroes(self, nums: List[int]) -> None:


        #Input: nums = [0,0,1,2,0,5]
        #               w   r                  
        # Output: [1,2,5,0,0,0]
                    
        # read/scan and write pointers


        write = 0 # # Next index where the next non-zero value should go.

        #  read visits every original element exactly once.
        for read in range(len(nums)):
            if nums[read] != 0: # check for non zero
                nums[write], nums[read] = nums[read], nums[write]
                write+=1



        # same thing in done in 2 phases

        # write = 0
        # # Phase 1: copy all non-zeros to the front, in order
        # for read in range(len(nums)):
        #     if nums[read] != 0:
        #         nums[write] = nums[read]
        #         write += 1
        # # Phase 2: fill the rest with zeros
        # for i in range(write, len(nums)):
        #     nums[i] = 0
  