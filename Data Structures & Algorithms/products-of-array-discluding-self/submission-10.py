class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [0]* n
        
        # prefix product
        result[0] = 1 # there is no prefix to the 0th index
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]


        # suffix product
        running_suffix_product = 1
        for i in range(n-1, -1, -1):
            result[i] = result[i] * running_suffix_product
            running_suffix_product *= nums[i]

        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        