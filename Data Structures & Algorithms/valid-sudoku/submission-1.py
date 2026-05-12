import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                value = board[r][c]
                sq_idx = (r//3,c//3)
                if (value in rows[r] or value in cols[c] or value in squares[sq_idx]):
                    return False
                
                rows[r].add(value)
                cols[c].add(value)
                squares[sq_idx].add(value)
        return True
            