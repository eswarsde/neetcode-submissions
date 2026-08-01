class Solution:
    # Dutch National Flag algorithm 
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # One idea
        # 1st pass: Count individial nums/colors in one pass
        # 2nd pass: rewrite the array, count of zeros, ones and then tows
        # 2 pases and o(n) for storing 

        #   # Dutch National Flag algorithm 

        # let's try to do in one pass with 2 pointers
        # divide array into 4 zones
        # zero zone, one zone, unsorted zone, two zone
        # this 4 zone can be managed by 3 varaibles 
        #  i and left, right pointers
        # i and left start at zero index and right on right most


        left = 0
        right = len(nums) - 1
        i = 0
        # now the entire array starts with one zone - unosrted array zone

        while i<=right:

            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i] # swap to the right most.. bcoz 2 zone is on the right
                right -=1 
                # i stays put, the value we rotate in is from unosrted middle and so we don't what value it is 
            elif nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left+=1
                i+=1 # moving i because we are keeping the zero zone is the left most zone i.e before the i pointer
            else: # i ==1
                i+=1  
                      






        