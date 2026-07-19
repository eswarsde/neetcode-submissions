class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hashmap
        # loop over and find the one

        seen = set()

        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return seen.pop()

        o(n), o(n)


        