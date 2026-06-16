class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()
        n = len(nums)
        target = 0

        for i in range(n-2): # n-2 because, we need triplets and the rest of the 2 elements will left and right pointers below
            if nums[i] > target:
                break # because we sorted, anything we add to "a" 
                #is ony going to make it bigger than our target zero

            if i > 0 and nums[i] == nums[i-1]:
                # i > 0 is needed because we are doing i-1 in the expressoin
                # why nums[i] == nums[i-1] ?
                  # if 2 contigious numbers are same, it's only going to produce duplicate 3sums
                  # example: nums = [-1, -1, 0, 1, 2]
                     # i = 0 -> [-1, 0, 1]
                     # i = 1  -> [-1, 0, 1]
                continue 
            
            left = i + 1
            right = n - 1
            

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1

                    # skip duplicates on left and right pointer similar to how we skipped a "i" with "continue"
                    while left < right and nums[left] == nums[left -1]:
                        left +=1

                elif total > target:
                    right -= 1
                else:
                    left += 1

                










        return result

        