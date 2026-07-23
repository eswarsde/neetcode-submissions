class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1 land
        # 0 water
        island_count = 0

        ROWS = len(grid)
        COLS = len(grid[0])
        visted = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):

            # bounday range check
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 

            # visited check
            if (r, c) in visted:
                return

            # stop if it's water # problem specifc condition
            if grid[r][c] == "0":
                return

            # mark visited
            visted.add((r, c))

            for dr, dc in directions:
                dfs(r+ dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visted:
                    dfs(r, c)
                    island_count+=1



        return island_count

# Time complexity: O(m∗n)
# Space complexity: O(m∗n) 
   # 1) The visited Set - In the worst-case scenario (where the entire grid is land), you will store every single cell coordinate in the set.
   # 2) The Recursion Call Stack (DFS) - In the worst case (e.g., the grid is filled with land in a single long snake-like shape), the recursion depth could go as deep as the total number of cells.