class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # intial idea -> DFS
        # identify start positions by scanning the grid and then DFS from there ??

        ROWS, COLS = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set() # Keeps track of (r, c) tuples used in the current path
       

        # intial idea -> DFS
        # identify start positions by scanning the grid and then DFS from there ??

        def dfs_backtracking(row, col, char_index):

            # base case
            if char_index == len(word):
                return True # we reached end of the word 

            # boundary check 
            if (row < 0 or col < 0 or 
                row >= ROWS or col >= COLS):
                return False

            # visited check 
            if (row, col) in visited:
                return False

            # problem logic # in this path, at this row,col/path, it should have the character "word[char_index]". if not path is invalid 
            if board[row][col] != word[char_index]:
                return False

            # mark visited 
            visited.add((row, col))

            # choices => choose => explore => unchoose
            for dr, dc in directions:
                if dfs_backtracking(row+dr, col+dc, char_index+1):
                    return True
            visited.remove((row, col))
            return False

        # find all start indexes and explore
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                     if dfs_backtracking(r, c, 0):
                        return True
        return False
        