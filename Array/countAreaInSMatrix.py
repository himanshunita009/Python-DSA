class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        minRow = minCol = 1000
        maxRow = maxCol = -1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    minRow = min(minRow,i)
                    minCol = min(minCol,j)
                    maxRow = max(maxRow,i)
                    maxCol = max(maxCol,j)
        return (maxRow-minRow+1)*(maxCol-minCol+1)
