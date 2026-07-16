class Solution:
    def twoSum(self, nums: List[int], target: int):

        seen = {} # num, index

        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [seen[needed], i]
            seen[num] = i
            
        return [-1, -1]
        
        
        



        
        
        # seen_index = {}

        # for index, val in enumerate(nums):
        #     diff = target - val
        #     if diff in seen_index:
        #         return [seen_index[diff], index]
        #     seen_index[val] = index

        # return [-1, -1]

        
