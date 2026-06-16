class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        best_max = nums[0]
        best_min = nums[0]
        current_max = 0
        current_min = 0
        total_sum = 0

        for num in nums:
            total_sum += num
            
            # 1. Maximize Subarray (Standard Kadane) 📈
            current_max = max(current_max, 0)
            current_max += num
            best_max = max(best_max, current_max)
            
            # 2. Minimize Subarray (Inverse Kadane) 📉
            current_min = min(current_min, 0)
            current_min += num
            best_min = min(best_min, current_min)

        # Edge case check
        if best_max < 0:
            return best_max
            
        return max(best_max, total_sum - best_min)

        