class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, columns = len(image), len(image[0])
        startColor = image[sr][sc]
        #Pruning: avoid meaningless path
        if startColor == color:
            return image
        
        def dfs(r, c):
            #Base case: when should return
            if r < 0 or r >= rows or c < 0 or c >= columns or image[r][c] != startColor:
                return
            #Recursive steps: change color & check neighborhood
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        dfs(sr, sc)
        return image