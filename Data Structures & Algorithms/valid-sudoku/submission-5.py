from collections import defaultdict

class Solution:
    def __init__(self):
        self.null = "."

    def check_row(self, board, x):
        row_dict = defaultdict(int)

        for n in board[x]:
            row_dict[n] += 1
            
            if n != self.null and row_dict[n] > 1:
                return False
        
        return True
            
    def check_col(self, board, y):
        col_dict = defaultdict(int)

        for i in range(len(board)):
            n = board[i][y]
            col_dict[n] += 1

            if n != self.null and col_dict[n] > 1:
                return False
        
        return True
        

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(9):
            r = self.check_row(board, x)
            if not r:
                return r
        
        for x in range(9):
            c = self.check_col(board, x)

            if not c: return c
        
        for quadrant in range(9):
            seen = set()
            for i in range(3):
                row = (quadrant // 3) * 3 + i
                for j in range(3):
                    col = (quadrant %  3) * 3 + j

                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    
                    seen.add(board[row][col])
        
        return True


        

