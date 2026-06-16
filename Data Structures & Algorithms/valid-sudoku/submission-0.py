class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check one row at a time
        for row in range(9): # rows
            seen = set()
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        # check for each column

        for col in range(9):
            seen = set()
            for row in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        # check each box # 0-2, 3-5, 6-8
        for box_row in range(0,9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for row in range(3):
                    for col in range(3):
                        val = board[box_row + row][box_col + col]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True

