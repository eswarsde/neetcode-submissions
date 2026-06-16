
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #  minimim integer such that you can eat all banana's in n hours

        """
        Input: piles = [1,4,3,2], h = 9

        Output: 2

        Brute Force:
        k = try all speeds 1...max(piles)=4
        
        Better Approach:
        binary search over k - try 2 first and see if we finish eating, and check the values on the left

        """
        def canFinishEating(speed):
            hours = 0

            for p in piles:
                hours += (p // speed)
                if p % speed != 0:
                    hours += 1
            
            return hours <= h

        left = 1
        right = max(piles)
        ans = right
        while left<=right:
            mid = (left + right)//2

            if canFinishEating(mid):
                right = mid -1
                ans = min(ans, mid)
            else: 
                left = mid + 1
        return ans
            


        