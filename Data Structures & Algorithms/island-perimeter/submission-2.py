from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        rows: int = len(grid)
        cols: int = len(grid[0])
        perimeter: int = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Start by assuming the land cell adds 4 to the perimeter
                    perimeter += 4
                    
                    # If there is land directly above, subtract the shared edge (2 sides)
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                        
                    # If there is land directly left, subtract the shared edge (2 sides)
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2
                        
        return perimeter

# The reason you only check **above** and **left** comes down to the direction of your `for` loops and avoiding double-counting shared edges.

# Because you are iterating through the grid from **top to bottom** and **left to right**, you only need to look *backward* at the cells you have already processed.

# Here is the step-by-step breakdown of why this works:

# ### 1. The Math of a Shared Edge

# When two land cells connect, they share exactly one edge. However, that shared edge means *both* cells lose one side of their perimeter. Therefore, every shared connection reduces the total theoretical perimeter by exactly 2.

# ### 2. The Traversal Order

# Imagine you have two adjacent land cells, **Cell A** (left) and **Cell B** (right):
# `[ A, B ]`

# * **When your loop is on Cell A:** You add 4 to the perimeter. You look above and left. There is nothing there.
# * **When your loop moves to Cell B:** You add 4 to the perimeter. You look left and see Cell A. Because you found a connection, you subtract 2 from the total perimeter.

# If you checked all four directions, you would subtract 2 when at Cell A (looking right at B) and then subtract 2 *again* when at Cell B (looking left at A). You would end up subtracting 4 for a single shared edge, which breaks the math.

# ### 3. The "Look Back" Strategy

# By consistently only looking **up** and **left**:

# * Every vertical connection is counted exactly once (when the bottom cell looks up).
# * Every horizontal connection is counted exactly once (when the right cell looks left).

# It is a clever optimization. Instead of meticulously checking all four boundaries for every single cell and keeping track of what has been counted, you just confidently walk forward and only check your blind spots to the rear.