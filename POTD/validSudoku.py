class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rowSet = [set() for _  in range(9)]
        colSet = [set() for _  in range(9)]
        for i in range(0,9,3):
            for j in range(0,9,3):
                temp = set()
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        if board[row][col] != '.':
                            num = ord(board[row][col])-ord('0')
                            if num in temp or num in rowSet[row] or num in colSet[col]:
                                return False
                            temp.add(num)
                            rowSet[row].add(num)
                            colSet[col].add(num)
        return True

obj = Solution()
print(obj.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))