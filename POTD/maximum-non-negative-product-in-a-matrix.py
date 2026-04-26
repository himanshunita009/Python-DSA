class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[0,0] for _ in range(m)] for _ in range(n)]
        mod = 10**9+7
        dp[0][0][0]=dp[0][0][1]=grid[0][0]
        for col in range(1,m):
            dp[0][col][0]= dp[0][col][1] = dp[0][col-1][0]*grid[0][col]
        for row in range(1,n):
            dp[row][0][0] = dp[row][0][1] = dp[row-1][0][0]*grid[row][0]
        
        for row in range(1,n):
            for col in range(1,m):
                x = grid[row][col]
                arr = (x*dp[row-1][col][0],x*dp[row-1][col][1],x*dp[row][col-1][0],x*dp[row][col-1][1])
                dp[row][col][0] = max(arr)
                dp[row][col][1] = min(arr)
        temp = dp[n-1][m-1][0]
        return temp%mod if temp >=0 else -1
        
obj = Solution()
print(obj.maxProductPath([[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]))