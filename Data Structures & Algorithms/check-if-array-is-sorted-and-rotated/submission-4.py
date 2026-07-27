class Solution:
    def check(self, nums: List[int]) -> bool:
        drop_count = 0
        n = len(nums)

        for i in range(n-1):
            #increasing order

            if nums[i] > nums[i+1]:
                drop_count +=1

                if drop_count > 1:
                    return False
            
        if nums[n - 1] > nums[0]:
            drop_count += 1

        return drop_count <= 1

        