class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen, res = {}, []
        for i, val in enumerate(nums):
            diff = target - val
            if diff in seen.keys():
                
                res.append(seen[diff])
                res.append(i)
                return res
            seen[val] = i
        return res 

        