class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Idea 1# with extra memory
        # have 2 pointers one for each array
        # at each iteration compare and take the smallest and append to the result array

        # Input: nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2
        # Output: [1,2,10,20,20,40]

       
       # Idea 2
        #without extra memory
        # Input: nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2

        # Output: [1,2,10,20,20,40]

        left = m -1 # last/largest element in nums1 
        right = n -1 # last/larges element in nums2
        write = m + n - 1  # write: next position to fill from the back of nums1

        while left >=0 and right >=0:
            if nums1[left] > nums2[right]:
                nums1[write] = nums1[left]
                left -=1
            else:
                nums1[write] = nums2[right]
                right-=1

            write -=1

        # # If nums2 still has leftover values, they must be copied.
        # # If nums1 has leftovers instead, they are already in correct sorted position.
        while right >=0:
            nums1[write] = nums2[right]
            right -=1
            write -=1









