class Solution:
    def __init__(self):
        self.rows = [0b111111111 for _ in range(9)]
        self.cols = [0b111111111 for _ in range(9)]
        self.square = [0b111111111 for _ in range(9)]
        self.found = False
        self.empty = []
        self.board = []

    def bit(self,n: str):
        return 1 << (int(n)-1)
    
        
    
    def solveSudoku(self, board: list[list[str]]) -> None:
        self.board = board
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    mask = ~self.bit(board[i][j])
                    self.rows[i] &= mask
                    self.cols[j] &= mask
                    self.square[(i // 3) * 3 + (j // 3)] &= mask
                else:
                    self.empty.append((i,j))
        def dfs(idx = 0):
            if idx == len(self.empty):
                return True
            best_option = None
            best_idx = -1
            min_count = 10
            for k in range(idx,len(self.empty)):
                i,j = self.empty[k]
                box = (i // 3) * 3 + (j // 3)
                mask = self.rows[i] & self.cols[j] & self.square[box]
                count = mask.bit_length()
                if count < min_count:
                    min_count = count
                    best_option = mask 
                    best_idx = k
                    if count == 1:
                        break

            if min_count == 0:
                return False
            self.empty[idx],self.empty[best_idx] = self.empty[best_idx], self.empty[idx]
            options = best_option
            i , j = self.empty[best_idx]
            box = (i // 3) * 3 + (j // 3)

            while options:
                dmask = options & -options
                options -= dmask

                d = str(dmask.bit_length())

                board[i][j] = d
                self.rows[i] ^= dmask
                self.cols[j] ^= dmask
                self.square[box] ^= dmask

                if dfs(idx+1):
                    return True 
                board[i][j] = '.'
                self.rows[i] ^= dmask
                self.cols[j] ^= dmask
                self.square[box] ^= dmask

            return False
    
        if dfs():
            print(board)
        

obj = Solution()
obj.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
    
                            
