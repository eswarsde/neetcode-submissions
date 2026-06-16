class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        counter = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                counter+=1
            else:
                best = max(best, counter)
                counter = 0

        return max(best, counter)
        