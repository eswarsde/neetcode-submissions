class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # DFS, DP Problem 
        # Return the length of the longest strictly increasing path within matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # You do not need a visited set for this specific problem because the strictly increasing constraint naturally prevents cycles.
        # In a typical matrix DFS (like finding the size of an island), you can move freely between adjacent valid cells. Without a visited set, your recursive function would get stuck in an infinite loop, endlessly bouncing back and forth between two neighbors.
        # However, in this problem, you can only move to a neighboring cell if its value is strictly greater than the current cell. This makes it mathematically impossible to travel backward or form a loop.

        # Cache to store the longest path starting from (r, c)
        memo: Dict[tuple[int, int], int] = {}

        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]

            result = 1 # Every single cell in the matrix counts as a valid path of at least length 1 (the cell itself)

            # Explore all 4 adjacent directions
            for dr, dc in directions:
                new_r, new_c = row + dr, col + dc

                # boundary check & is the previous value seen bigger than current value 
                if (0 <= new_r < ROWS and 0 <= new_c < COLS and matrix[new_r][new_c] > matrix[row][col]):
                    result = max(result, 1 + dfs(new_r, new_c))
                    # The dfs(new_r, new_c) function call returns the length of the longest path starting from your neighbor's cell
                    # Since you are stepping from your current cell into that neighboring cell, you have to add 1 to account for the current cell in the total path length.
            memo[(row, col)] = result
            return result
  


        longest_increasing_path = 0     
        # outer loop: Handle disconnected components
        for r in range(ROWS):
            for c in range(COLS):
                longest_increasing_path = max(longest_increasing_path, dfs(r, c))

        return longest_increasing_path
        