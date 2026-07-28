class Solution:
    def twoSum(self, nums: List[int], target: int):

        seen_at_index = {}

        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen_at_index:
                return[seen_at_index[needed], i]
            else:
                seen_at_index[num] = i
        return [-1, -1]



        
