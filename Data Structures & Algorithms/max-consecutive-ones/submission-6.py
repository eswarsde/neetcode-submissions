class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        best = 0
        count = 0

        for num in nums:
            if num==1:
                count+=1
            else:
                best = max(count, best)
                count = 0

        return max(best, count)
        
        
        
        
        
        
        
        # best = 0
        # counter = 0
        # for i in range(0, len(nums)):
        #     if nums[i] == 1:
        #         counter+=1
        #     else:
        #         best = max(best, counter)
        #         counter = 0

        # return max(best, counter)
        