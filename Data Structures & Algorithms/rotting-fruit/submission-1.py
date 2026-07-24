from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        0 -> empty
        1 -> fresh
        2 -> rotten
        
        directions we can rot: all 4

        return: return how many mins
        
        matrix: DFS or BFS
        # BFS is a better match because, the rotten oranges will contaminate their neighbors first(immediate level)
        # BFS is level by level => minute by minute
        """

        """
        starting point: generally we start at one starting point, but here we have multiple rotten friuts that we need to start at the same time
        # counter of fresh fruits - when reaches zero, we end the loop and return minutes
        # go through all the rotten fruit once and mark it's negihbours as rotten 

        """

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = deque()
        fresh_fruits_count = 0
        minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_fruits_count += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        if fresh_fruits_count == 0:
            return 0

        while queue:
            num_nodes_at_level = len(queue)
            rotten_this_minute = False

            for _ in range(num_nodes_at_level):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    # within bounds
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >=COLS:
                        continue

                    # not fresh 
                    if grid[nr][nc] != 1:
                        continue

                    # rot this matrix
                    grid[nr][nc] = 2
                    fresh_fruits_count -=1 # reduce the count
                    queue.append((nr, nc)) # Append the rotten back queue for next level
                    rotten_this_minute = True

            if rotten_this_minute:
                minutes+=1

        if fresh_fruits_count > 0:
            return -1
        
        return minutes



        


        


        return -1
        