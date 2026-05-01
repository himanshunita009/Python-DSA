class Solution:
    def solve(self,row : int,col:int , grid: list[list[int]],mp: dict):
        n = len(grid)
        m = len(grid[0])
        if row == n-1 and col == m-1:
            return True
        original = grid[row][col]
        grid[row][col] = 7
        for cell in mp[original]:
            dr , dc = cell
            newRow = row+dr 
            newCol = col+dc
            if n > newRow  >= 0 and m > newCol >= 0 and grid[newRow][newCol] != 7:
                for cell1 in mp[grid[newRow][newCol]]:
                    if cell1[0]+dr == 0 and cell1[1]+dc == 0:
                        if self.solve(newRow,newCol,grid,mp):
                            return True
        return False
                

    def hasValidPath(self, grid: list[list[int]]) -> bool:
        n =len(grid)
        m =len(grid[0])
        mp = dict()
        mp[1] = [[0,-1],[0,1]]
        mp[2] = [[-1,0],[1,0]]
        mp[3] = [[0,-1],[1,0]]
        mp[4] = [[0,1],[1,0]]
        mp[5] = [[-1,0],[0,-1]]
        mp[6] = [[-1,0],[0,1]]
        return self.solve(0,0,grid,mp)
    

Obj= Solution()
print(Obj.hasValidPath([[2,4,3],[6,5,2]]))
    
            
