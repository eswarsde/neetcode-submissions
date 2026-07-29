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