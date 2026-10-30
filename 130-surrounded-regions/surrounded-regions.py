class Solution:
    # Only the 'O' regions that touch the border can never be surrounded
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        # modify board to mark ->  don't need to record visit status
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 1️⃣ Mark all border-connected 'O' cells as “#” 
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or board[r][c] != 'O':
                return
            board[r][c] = '#'
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # 2️⃣ Start from every border cell that is 'O', mark all border-connected cells
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)
        
        # 3️⃣ Scan entire board: not border-connected cells -> 'X'
        #       border-connected cells -> 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'