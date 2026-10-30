class Solution:
    # ------------ TC & SC: O(M * N) ------------
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        # adjacent cells
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # record visit to avoid infinite loop
        pacific = set()
        atlantic = set()

        # add all valid coordinate into the set
        def dfs(r, c, ocean_set):
            ocean_set.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # skip 'out of borders' and 'has visited', and find higher location where water can flow from
                if nr not in range(rows) or nc not in range(cols):
                    continue
                if (nr, nc) in ocean_set:
                    continue
                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, ocean_set)

        # check from each cell of 4 borders   
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)
        
        # get the intersection and convert it into list
        return list(pacific & atlantic)
            
