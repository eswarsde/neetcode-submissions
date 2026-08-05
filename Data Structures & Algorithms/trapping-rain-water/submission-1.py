class Solution:
    # https://www.hellointerview.com/learn/code/two-pointers/trapping-rain-water
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

# def trappingWater(heights):
#     if not heights:
#         return 0
#     left, right = 0, len(heights) - 1
#     leftMax, rightMax = heights[left], heights[right]
#     count = 0
    
#     while left < right:
#         if leftMax < rightMax:
#             left += 1
#             if heights[left] >= leftMax:
#                 leftMax = heights[left]
#             else:
#                 count += leftMax - heights[left]
#         else:
#             right -= 1
#             if heights[right] >= rightMax:
#                 rightMax = heights[right]
#             else:
#                 count += rightMax - heights[right]
    
#     return count