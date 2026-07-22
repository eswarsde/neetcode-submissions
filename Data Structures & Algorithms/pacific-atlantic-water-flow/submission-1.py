class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac_reachable, atl_reachable = set(), set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        result = []

        def dfs(r, c, visited, prev_height):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            
            # stop 
            if (r, c) in visited:
                return
            # water can only from high/same level to current cell
            current_height = heights[r][c]
            if current_height < prev_height:
                return


            # visited
            visited.add((r, c))
            # recurse in all 4 directions
            for dr, dc in directions:
                dfs(r+dr, c+dc, visited, heights[r][c])


        # Walk down the left (Pacific) and right (Atlantic) edges
        for r in range(ROWS):
            dfs(r, 0, pac_reachable, heights[r][0])
            dfs(r, COLS - 1, atl_reachable, heights[r][COLS - 1])

        # Walk across the top (Pacific) and bottom (Atlantic) edges
        for c in range(COLS):
            dfs(0, c, pac_reachable, heights[0][c])
            dfs(ROWS - 1, c, atl_reachable, heights[ROWS - 1][c])


        #                         pac_reachable.intersection(atl_reachable)
        return [[r, c] for r, c in pac_reachable & atl_reachable]

        