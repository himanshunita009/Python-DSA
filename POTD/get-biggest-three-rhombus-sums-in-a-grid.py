class Solution:
    def isValid(self,point: tuple):
        return self.n > point[0] >= 0 and self.m > point[1] >= 0
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        self.n = len(grid)
        self.m = len(grid[0])
        dp = set()
        for i in range(self.n):
            for j in range(self.m):
                dp.add(grid[i][j])
                for k in range(1,min(self.n,self.m)//2+1):
                    leftPoint = (i+k,j-k)
                    rightPoint = (i+k,j+k)
                    bottomPoint = (i+2*k,j)
                    if  self.isValid(leftPoint) and self.isValid(rightPoint) and self.isValid(bottomPoint):
                        ans = grid[i][j]

                        # top -> left
                        for d in range(1, k+1):
                            ans += grid[i+d][j-d]

                        # left -> bottom
                        for d in range(1, k+1):
                            ans += grid[i+k+d][j-k+d]

                        # top -> right
                        for d in range(1, k+1):
                            ans += grid[i+d][j+d]

                        # right -> bottom
                        for d in range(1, k+1):
                            ans += grid[i+k+d][j+k-d]
                        dp.add(ans)
        dp = list(dp)
        dp.sort(reverse=True)
        return dp[:3]
        
                        
                        
                    