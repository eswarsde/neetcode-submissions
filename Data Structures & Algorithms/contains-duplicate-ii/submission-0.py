class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        if k <=0:
            return False

        last_seen = {}

        for index, val in enumerate(nums):

            if val in last_seen:
                # calculate abs(i - j) <= k

                dist = abs(index - last_seen[val])

                if dist <=k:
                    return True
            
            last_seen[val] = index
        return False


        