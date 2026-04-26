class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        mod = 12345
        zeroCount = 0
        modCount = 0
        n = len(grid)
        m = len(grid[0])
        product = 1
        zeroIdx = -1
        modIdx = -1
        
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0:
                    zeroCount += 1
                    zeroIdx = (row,col)
                elif grid[row][col] == mod:
                    modCount += 1
                    modIdx = (row,col)
                if zeroCount == 2 or modCount == 2 or (zeroCount > 0 and modCount > 0):
                    return [[0]*m for _ in range(n)]
                if grid[row][col] != 0 and grid[row][col] != mod: 
                    product *= grid[row][col]
        ans = [[0]*m for _ in range(n)]
        if zeroIdx != -1:
            ans[zeroIdx[0]][zeroIdx[1]] = product
            return ans
        elif modCount != -1:
            ans[modIdx[0]][modCount[1]] = product
            return ans
        for row in range(n):
            for col in range(m):
                ans[row][col] = (product//grid[row][col])%mod
        return ans