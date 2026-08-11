class Solution:
    def maxScore(self, s: str) -> int:
        # rough idea
        # pre calcualte prefix_zero_count and suffix_one_count 
        # and then loop to fiure out max score

        n = len(s)

        # We use size 'n' instead of 'n + 1' because the problem requires 
        # NON-EMPTY substrings. We will never need a buffer for 0 elements.
        left_zero_count = [0] * (n)
        right_one_count = [0] * (n)

        for idx, char in enumerate(s):
            zero_count = 0
            if idx > 0:
                zero_count = left_zero_count[idx - 1] # previous
            if char == "0":
                zero_count+=1
            left_zero_count[idx] = zero_count
        
    
        for idx in range(n -1, -1, -1):
            char = s[idx]
            one_count = 0
            if idx < n - 1:
                one_count = right_one_count[idx + 1] # previous on the right side
            if char == "1":
                one_count+=1
            right_one_count[idx] = one_count

        bestScore = 0

        for i in range(1, n):
            # Since your left substring stops right before the split point i, its very last character is sitting at index i - 1
            # Since your right substring starts exactly at the split point i, we want the count of ones starting from i all the way to the end.
            bestScore = max(bestScore, left_zero_count[i - 1] + right_one_count[i])

        return bestScore
    