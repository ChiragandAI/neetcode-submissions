import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return not self.check_row(board) and not self.check_col(board) and not self.check_box(board)
    
    def check_row(self,board):
        return sum([self.check_duplicates(lst) for lst in board])
    
    def check_col(self,board):
        board_t = np.array(board).T
        return sum([self.check_duplicates(lst) for lst in list(board_t)])
    
    def check_box(self,board):
        final = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                temp = []
                for n in board[i:i+3]:
                    temp = temp + n[j:j+3] 
                final.append(self.check_duplicates(temp))
        return sum(final)
        

    def check_duplicates(self,nums: List[str]) -> bool:
        counter = {}
        for el in nums:
            counter[el] = 1 + counter.get(el,0)

        for k,v in counter.items():
            if k != "." and v > 1:
                return True
        return False