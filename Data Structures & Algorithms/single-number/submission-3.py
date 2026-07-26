class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # XOR 
        # X ^ X = 0 and X ^ 0 = X,
        #  the duplicate 3s canceled each other out.
        res = 0
        for num in nums:
            res = num ^ res
        return res
        # hashmap
        # loop over and find the one

        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         seen.remove(num)
        #     else:
        #         seen.add(num)
        
        # return seen.pop()

        # # o(n), o(n)


        