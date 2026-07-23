

from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
             return 0
         # minimim number of steps -> BFS
        # 1. Symmetry optimization: Only search the first quadrant
        # Imagine you are standing at the center of an infinitely large, empty parking lot (your (0,0) starting point).
        #  If I tell you to take exactly 3 knight leaps to the North-East, you will end up at some specific coordinate.
       # If I tell you to take those exact same 3 leaps, but mirror them to the South-West, you will end up at a negative coordinate, but the effort (3 leaps) was exactly the same.

        # Because an infinite chessboard has no edges, the board is perfectly mirrored across both the X and Y axes.

            # Path to (5, 5) takes N steps.

            # Path to (-5, 5) takes N steps.

            # Path to (5, -5) takes N steps.

            # Path to (-5, -5) takes N steps.

            # Why do we care?
            # In a standard BFS, your knight expands outward in a massive circle, checking all 8 directions at every single step. The queue grows exponentially: 1 node -> 8 nodes -> 64 nodes -> 512 nodes.

            # If your target is way up in the top-right corner at (200, 200), standard BFS will waste thousands of calculations sending knights deep into the bottom-left corner (-200, -200). Those knights are running entirely in the wrong direction!
        x, y = abs(x), abs(y) 

        knight_moves = [[+2, +1], [+2, -1], [-2, +1], [-2, -1], [+1, +2], [+1, -2], [-1, +2], [-1, -2]]

         # start [(0,0)]
        queue = deque([(0,0)])
        visited = set()
        visited.add((0, 0))
    
        steps_needed = 0

        while queue:
            num_nodes_in_level= len(queue)

            for _ in range(num_nodes_in_level):
                curr_node_x, curr_node_y = queue.popleft()

                if curr_node_x == x and curr_node_y == y:
                    return steps_needed
                

                for dx, dy in knight_moves:
                    next_node_x = curr_node_x + dx
                    next_node_y = curr_node_y + dy

                    if (next_node_x, next_node_y) not in visited and -2 <= next_node_x <= x + 2 and -2 <= next_node_y <= y + 2: 
                        visited.add((next_node_x, next_node_y))
                        queue.append((next_node_x, next_node_y))
            steps_needed+=1 
        return -1
           



    






        