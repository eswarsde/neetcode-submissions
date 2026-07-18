class Solution:
    def mySqrt(self, x: int) -> int: 
        left, right = 0, x
        result = 0


        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square > x:
                right = mid -1
            elif square < x:
                left = mid + 1
                result = mid # keep storing the temp result until we find the closest
            else:
                return mid # exact sqrt, return immediately

        return result
        
        # 64 - 8


        