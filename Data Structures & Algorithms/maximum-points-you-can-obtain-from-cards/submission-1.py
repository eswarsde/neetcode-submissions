class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # the idea is sliding window covers all the elements that is not contributing to maxScore
        # [1, 2, 3, 4, 5, 6] => k= 3
        #     |     | 
        #     -------

        left = 0
        right = len(cardPoints) - k # (6 -3) = 3
        window_sum = sum(cardPoints[right:]) # 0 to 3
        best = window_sum

        while right < len(cardPoints):
            # Move one card from the right-chosen group to the left-chosen group.
            window_sum += cardPoints[left] - cardPoints[right] # as we move the window right
            best = max(best, window_sum)
            left+=1 # moving wondow towards right means we increase both left and right by 1
            right+=1
        
        return best