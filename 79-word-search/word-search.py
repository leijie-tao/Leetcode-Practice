class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])
        def backtrack(row, column, pos):
            if pos == len(word): #终止条件：字母全部匹配成功
                return True
            if (row < 0 or row >= rows or column < 0 or column >= columns or board[row][column] != word[pos]): #边界检查
                return False

            temp = board[row][column] #利用temp记录回溯的位置
            board[row][column] = '#'
            res = (backtrack(row + 1, column, pos + 1) or
                   backtrack(row - 1, column, pos + 1) or
                   backtrack(row, column + 1, pos + 1) or
                   backtrack(row, column - 1, pos + 1)) #向四个方向探索, 只要有一条路通了，就说明找到了
            board[row][column] = temp #回溯至记录点
            return res

        for r in range(rows):
            for c in range(columns):
                if backtrack(r, c, 0):
                    return True
        
        return False
