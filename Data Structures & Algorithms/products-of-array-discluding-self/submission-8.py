class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len  = len(nums)
        prefix = [1] * nums_len
        suffix = [1] * nums_len
        result = [1] * nums_len

        prefix[0] =1 
        suffix[-1]=1
        
        
        for i in range(1, nums_len):
            prefix[i] = nums[i-1] * prefix[i-1]

        for i in range(nums_len -2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1] 

        for i in range(nums_len):
            result[i] = prefix[i]*suffix[i]

        return result



        