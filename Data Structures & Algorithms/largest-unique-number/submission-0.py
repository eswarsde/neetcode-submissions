class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = {} # o(n)

        # O(n)
        for num in nums:
            if num in count:
                count[num] +=1
            else:
                count[num] = 1

        result = -1

        # O(n)
        for val, count in count.items():
            if count == 1:
                if val > result:
                    result = val

        return result 