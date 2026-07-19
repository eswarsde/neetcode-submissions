class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
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