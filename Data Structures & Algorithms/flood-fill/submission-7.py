class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        
        if original_color == color:
            return image

        ROWS, COLS = len(image), len(image[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            if r < 0 or r >=ROWS or c < 0 or c >=COLS:
                return 

            # only need to change colors of neighbours that has same color as image[sr][sc] i.e original_color
            if image[r][c] != original_color:
                return
            image[r][c] = color
            for dr, dc in directions:
                dfs(r+dr, c+dc)
    
            
        dfs(sr, sc)
        return image

# Time complexity: O(m∗n)
# Space complexity: O(m∗n)