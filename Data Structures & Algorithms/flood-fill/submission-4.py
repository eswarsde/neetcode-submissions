class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        
        if original_color == color:
            return image

        ROWS, COLS = len(image), len(image[0])

        def dfs(r, c):
            if r < 0 or r >=ROWS or c < 0 or c >=COLS:
                return 

            # only need to change colors of neighbours that has same color as image[sr][sc] i.e original_color
            if image[r][c] != original_color:
                return
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c +1)
            dfs(r, c-1)

            
        dfs(sr, sc)
        return image