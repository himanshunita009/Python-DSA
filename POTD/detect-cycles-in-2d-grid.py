class Solution:
    def solve(self,row: int,col: int,parent: list[int],grid: list[list[str]],visited: list[list[bool]]):
        visited[row][col] = True
        dr = [-1,1,0,0]
        dc = [0,0,1,-1]
        for idx in range(4):
            newRow = row+dr[idx]
            newCol = col+dc[idx]
            if len(grid) > newRow >= 0 and len(grid[0]) > newCol >= 0 and grid[newRow][newCol] == grid[row][col]:
                if visited[newRow][newCol]:
                    if [newRow,newCol] != parent:
                        return True
                else:
                    if self.solve(newRow,newCol,[row,col],grid,visited):
                        return True
        visited[row][col] = False
        return False


    def containsCycle(self, grid: list[list[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        visited = [[False]*m for _ in range(n)]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.solve(row,col,[-1,-1],grid,visited):
                    return True
        return False

obj = Solution()
print(obj.containsCycle([["a","b","b"],["b","z","b"],["b","b","a"]]))

