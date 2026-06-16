class Solution:
    def twoSum(self, nums: List[int], target: int):
        seen_index = {}

        for index, val in enumerate(nums):
            diff = target - val
            if diff in seen_index:
                return [seen_index[diff], index]
            seen_index[val] = index

        return [-1, -1]

        
