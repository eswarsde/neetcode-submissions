
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            maxArea = max(maxArea, area)
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxArea


        # max_area = 0
        # left, right = 0, len(heights)-1

        # while left < right:
        #     width = right - left
        #     height = min(heights[left], heights[right])
        #     area = width * height
        #     max_area = max(max_area, area)

        #     if heights[left] < heights[right]:
        #         left +=1
        #     else:
        #         right -=1
        # return max_area



        