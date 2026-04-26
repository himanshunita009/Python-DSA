class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        tSum = 0
        temp = []
        n = len(grid)
        m = len(grid[0])
        for row in range(n):
            temp.append(grid[row].copy())
            for col in range(m):
                tSum += grid[row][col]
                grid[row][col] = tSum
        if tSum&1:
            return False
        target = tSum//2
        grid,temp = temp,grid
        tSum = 0
        for col in range(m):
            for row in range(n):
                tSum += grid[row][col]
                grid[row][col] = tSum
                if tSum == target or temp[row][col] == target:
                    return True
        return False

obj = Solution()
print(obj.canPartitionGrid([[1,4],[2,3]]))