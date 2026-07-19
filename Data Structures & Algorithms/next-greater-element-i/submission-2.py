class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        result = []
        for num in nums1:
            for i, unique_num in enumerate(nums2):
                if num == unique_num: # found where num lives in nums2
                    next_greater = -1
                    for j in range(i+1, n):
                        if nums2[j]> num:
                             next_greater = nums2[j]
                             break
                    result.append(next_greater)
                    break
                        
    
        return result
                        
                        


