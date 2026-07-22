class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        """
        In order to solve this problem, we can first recognize that there are two types of "Os" in the grid,
            those that are reachable on a path of connected "O"s starting from the border of the grid, and those that are not.

        step 1:
        This means that we can start from each cell in the border of the grid and use depth-first search to find all the "Os" that are reachable from the border of the grid
         (by following a path of connected "Os" in the N, E, S, W directions). 
        Whenever we find an "O" that is reachable from the border, we can change its value to "S" to mark it as safe.

        step 2:
        After marking them as safe,
        we can then iterate through each cell in the grid and change the "Os" that are not marked as safe to "Xs", while also changing the "safe" cells back to "Os".

        """

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 
            
            if board[r][c] != "O":
                return 

            board[r][c] = "S"

            for dr, dc in directions:
                dfs(r + dr, c + dc)


        # Step 1: 
        for r in range(ROWS):
            if board[r][0]=="O":
                dfs(r, 0)
            if board[r][COLS-1]=="O":
                dfs(r, COLS-1)
        
        for c in range(COLS):
            if board[0][c]=="O":
                dfs(0,c)
            if board[ROWS-1][c]=="O":
                dfs(ROWS-1, c)

        # Step 2:      
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]== "O":
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
                


# Time complexity: O(m∗n)
# Space complexity: O(m∗n)

