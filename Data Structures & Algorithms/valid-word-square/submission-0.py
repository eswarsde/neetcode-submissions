class Solution:

    # for every position (row, col), the character must equal the character at position (col, row)
    def validWordSquare(self, words: List[str]) -> bool:
        numRows = len(words)

        for r in range(numRows):
            for c in range(len(words[r])):
                
                # Check for 'out of bounds' in the transposed position:
                # 1. If you are at row r, column c, but there isn't even a row at index c, it can't be a word square.
                # 2. If row c exists but is too short to have a character at index r, the symmetry is broken.
                if c >= numRows or r >=len(words[c]):
                    return False

                # Check if the characters match
                if words[r][c] != words[c][r]:
                    return False
        return True
        
        
# To improve readability, we can rename the variables to reflect their positions in the matrix (rows and columns). In a word square, the fundamental rule is that the character at `words[r][c]` must be the same as the character at `words[c][r]`.

# Here is a more readable version of the logic:

# ```python
# class Solution:
#     def validWordSquare(self, words: List[str]) -> bool:
#         num_rows = len(words)
        
#         for r in range(num_rows):
#             # Iterate through each character in the current row word
#             for c in range(len(words[r])):
                
#                 # Check for 'out of bounds' in the transposed position:
#                 # 1. Does the corresponding row 'c' even exist?
#                 # 2. If it exists, is it long enough to have a character at index 'r'?
#                 if c >= num_rows or r >= len(words[c]):
#                     return False
                
#                 # Check if the characters match
#                 if words[r][c] != words[c][r]:
#                     return False
                    
#         return True
# ```

# ### Why these checks are necessary:
# Because the input is a list of strings and not a perfect $N \times N$ matrix, we must handle "jagged" arrays:
# 1.  `c >= num_rows`: If you are at row `r`, column `c`, but there isn't even a row at index `c`, it can't be a word square.
# 2.  `r >= len(words[c])`: If row `c` exists but is too short to have a character at index `r`, the symmetry is broken.
# 3.  `words[r][c] != words[c][r]`: The actual character comparison.

# ### Complexity:
# *   **Time Complexity:** $O(N \cdot M)$, where $N$ is the number of words and $M$ is the average length of the words. We visit each character in the input once.
# *   **Space Complexity:** $O(1)$, as we are only using a few pointers and checking the input in place.