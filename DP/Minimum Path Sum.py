class Solution:
    def solve(self,row  : int,col: int, grid: list[list[int]],dp):
        if dp[row][col] != -1:
            return dp[row][col]
        dp[row][col] = min(self.solve(row-1,col,grid,dp),self.solve(row,col-1,grid,dp)) + grid[row][col]
        return dp[row][col]
    def minPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(1,n):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        for j in range(1,m):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        return self.solve(n-1,m-1,grid,dp)
