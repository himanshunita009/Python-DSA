class Solution:
    def countUnguarded(self, n: int, m: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0]*m for _ in range(n)]
        for [row,col] in walls:
            grid[row][col] = 2
        for [row,col] in guards:
            grid[row][col] = 2
        ans = 0 
        for [row,col] in guards:
            for newRow in range(row-1,-1,-1):
                if grid[newRow][col] == 2:
                    break
                elif grid[newRow][col] == 0:
                    grid[newRow][col] = 1
                    ans += 1
            for newRow in range(row+1,n):
                if grid[newRow][col] == 2:
                    break
                elif grid[newRow][col] == 0 :
                    grid[newRow][col] = 1
                    ans += 1
            
            for newCol in range(col-1,-1,-1):
                if grid[row][newCol] == 2:
                    break
                elif grid[row][newCol] == 0 :
                    grid[row][newCol] = 1
                    ans += 1
            for newCol in range(col+1,m):
                if grid[row][newCol] == 2:
                    break
                elif grid[row][newCol] == 0 :
                    grid[row][newCol] = 1
                    ans += 1
        return n*m - ans - (len(guards)+len(walls))


obj = Solution()
print(obj.countUnguarded(4, 6,[[0,0],[1,1],[2,3]],[[0,1],[2,2],[1,4]]))