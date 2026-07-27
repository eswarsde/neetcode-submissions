class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Input: nums1 = [4,1,2], nums2 = [1,3,4,2]

        # Output: [-1,3,-1]

        # Naive way: nested loop 

        # for each num in nums 1
        #   * find the match index in nums 2
        #   * then continue right to find the greater element
          # if no return -1

    #  # Store the final answers in the same order as nums1.
    #     result = []
    
    #     for target in nums1:

    #         answer = -1
            
    #         found_target = False
            
    #         for num in nums2:

    #             if not found_target:
    #                 if num == target:
    #                     found_target = True
    #             else:
    #                 if num > target:
    #                     answer = num
    #                     break
            
    #         result.append(answer)
        
    #     # Return all answers in nums1 order.
    #     return result

    #    # Time complexity: O(len(nums1) * len(nums2))
    #    # Space Complexity: O(len(nums1))


       # Idea 2:
        next_greater_lookup = {}

        stack = []

        # Pre-porcess nums2
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater_lookup[smaller] = num
            
            stack.append(num)

        while stack:
            leftover = stack.pop()
            next_greater_lookup[leftover] = -1
        
        ans = []

        for num in nums1:
            ans.append(next_greater_lookup[num])

        return ans

            




