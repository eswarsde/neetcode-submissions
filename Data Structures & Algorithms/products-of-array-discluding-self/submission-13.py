class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # start with 1 not zero because zero can make all products zero
        result = [1] * (len(nums))

        running_product_prefix = 1
        for idx, num in enumerate(nums):
            # Except Self: Store and then Update
            result[idx] = running_product_prefix
            running_product_prefix *= num

        running_product_suffix = 1
        for idx in range(n-1, -1, -1):
            # Except Self: Store and then Update
            result[idx] *= running_product_suffix
            running_product_suffix *= nums[idx]
        
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        