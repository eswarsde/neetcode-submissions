class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_index = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen_index:
                return [seen_index[diff], index]
            seen_index[num] = index

        