class Solution:
    def isVisited(self,row,col):
        return self.visited[row][col]
    def numIslands(self, grid: list[list[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        self.visited = [[False]*m for _ in range(n)]
        self.grid = grid
        ans = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1" and not self.visited[row][col]:
                    self.visited[row][col] = True
                    self.solve(row,col)
                    ans += 1
        return ans
    def isValid(self,row: int,col: int):
        return len(self.visited) > row >= 0 and len(self.visited[0]) > col >= 0 and self.grid[row][col] == "1" and not self.visited[row][col]

    def solve(self,row: int,col: int): 
        dr = [0,0,-1,1]
        dc = [1,-1,0,0]
        for idx in range(4):
            newRow = dr[idx] + row
            newCol = dc[idx] + col
            if self.isValid(newRow,newCol):
                self.visited[newRow][newCol] = True
                self.solve(newRow,newCol)

