class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1 sort
        target = 0
        len_ = len(nums)
        if len_ < 3:
            return []
        if len_ == 3:
            if sum(nums) == target:
                return [nums]
            return []

        nums.sort() # T: o(nlogn)

        if nums[-1] < 0: # last num of array is negative after sorting, no way we get target zero by adding anything 
            return []

        result = []
        for i in range(len_ - 2): 
            
            if nums[i] > 0: # if the element we are in already greater than target, then no point in trying beyond this as we sorted the array already 
                break
            
            left = i + 1
            right = len_ - 1

            if i > 0 and nums[i] == nums[i-1]: # afer the first iteration, i.e i > 0, whenever we encoutner the same duplicate num, skip iteration, increment i by 1 until we see non duplicate number
                continue

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # see explanation in soluetion below tp see why we are only moving left 
                    while left < right and nums[left] == nums[left -1]:
                        left +=1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result


        # result = []
        # nums.sort()
        # n = len(nums)
        # target = 0

        # for i in range(n-2): # n-2 because, we need triplets and the rest of the 2 elements will left and right pointers below
        #     if nums[i] > target:
        #         break # because we sorted, anything we add to "a" 
        #         #is ony going to make it bigger than our target zero

        #     if i > 0 and nums[i] == nums[i-1]:
        #         # i > 0 is needed because we are doing i-1 in the expressoin
        #         # why nums[i] == nums[i-1] ?
        #           # if 2 contigious numbers are same, it's only going to produce duplicate 3sums
        #           # example: nums = [-1, -1, 0, 1, 2]
        #              # i = 0 -> [-1, 0, 1]
        #              # i = 1  -> [-1, 0, 1]
        #         continue 
            
        #     left = i + 1
        #     right = n - 1
            

        #     while left < right:
        #         total = nums[i] + nums[left] + nums[right]
        #         if total == target:
        #             result.append([nums[i], nums[left], nums[right]])
        #             left +=1
        #             right -=1

        #             # only skip duplicates on the left pointer why
        #             # If you force nums[left] to be a brand new number, 
        #             # the next valid triplet is mathematically guaranteed to be unique. 
        #             # You don't strictly need to skip duplicates on right as well,
        #             # because changing just one piece of the equation (nums[left])
        #             # guarantees the whole [nums[i], nums[left], nums[right]] combination will be different.
        #             while left < right and nums[left] == nums[left -1]:
        #                 left +=1

        #         elif total > target:
        #             right -= 1
        #         else:
        #             left += 1


        # return result

        