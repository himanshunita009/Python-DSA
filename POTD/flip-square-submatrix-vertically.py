class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        for col in range(y,y+k):
            for row in range(x,(x+k+1)//2):
                grid[row][col] , grid[x+k-row][col] = grid[x+k-row][col], grid[row][col] 
        return grid
    
obj = Solution()
print(obj.reverseSubmatrix([[3,4,2,3],[2,3,4,2]],0,2,2))