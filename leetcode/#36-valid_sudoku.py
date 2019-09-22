""" Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

 """
class Solution:
    def isValidSudoku(self, board):
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                if c == '.':
                    continue
                if (i,c) in seen or (c, j) in seen or (3*(i//3), 3*(j//3),c) in seen:
                    return False
                seen.add((i,c))
                seen.add((c,j))
                seen.add((3*(i//3),3*(j//3),c))
                #print(seen)
                #print((i,c),(c,j),(i/3,j/3,c))
        print(seen)
        return True

data = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]


sol = Solution()
print(sol.isValidSudoku(data))




