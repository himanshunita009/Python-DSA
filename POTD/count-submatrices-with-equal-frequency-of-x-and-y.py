class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        grid = [[(1 if grid[row][col] == "X"else 0,1 if grid[row][col] == "Y" else 0) for col in range(m)] for row in range(n)]
        grid.insert(0,[(0,0)]*m)
        ans = 0
        for row in range(1,n+1):
            countX = grid[row][0][0] + grid[row-1][0][0]  
            countY = grid[row][0][1] + grid[row-1][0][1]
            grid[row][0] = (countX,countY)
            if grid[row][0][0] == grid[row][0][1] and grid[row][0][0] > 0:
                ans += 1  
            for col in range(1,m):
                countX = grid[row][col][0] + grid[row-1][col][0]+grid[row][col-1][0]-grid[row-1][col-1][0]
                countY = grid[row][col][1] + grid[row-1][col][1]+grid[row][col-1][1]-grid[row-1][col-1][1]
                grid[row][col] = (countX,countY)
                if grid[row][col][0] == grid[row][col][1] and grid[row][col][0] > 0:
                    ans += 1    
        return ans
obj = Solution()
print(obj.numberOfSubmatrices([["X","Y","."],["Y",".","."]]))

# class Solution:
#     def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
#         if grid[0][0] > k:
#             return 0
#         n = len(grid)+1
#         m = len(grid[0])
#         ans = 0
#         grid.insert(0,[0]*m)
#         for row in range(1,n):
#             grid[row][0] += grid[row-1][0]
#             if grid[row][0] <= k:
#                 ans += 1
#                 grid[row][0]
#             else:
#                 break
#             for col in range(1,m):
#                 grid[row][col] = grid[row][col]+grid[row][col-1]+grid[row-1][col] - grid[row-1][col-1]
#                 if grid[row][col] <= k:
#                     ans += 1 
#         return ans