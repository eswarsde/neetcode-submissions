class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        min_len = n + 1 
        window_sum = 0
        left = 0

        for right in range(n):
            window_sum += nums[right]

            while window_sum>= target:
                current_len = right - left + 1

                if current_len < min_len:
                    min_len = current_len
                
                window_sum -=nums[left]

                left +=1

        if min_len == n + 1:
            return 0


        return min_len    