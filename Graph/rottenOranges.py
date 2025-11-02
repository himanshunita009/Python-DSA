from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque()
        cnt = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
        ans = 0
        if cnt == 0:
            return 0
        while len(queue) > 0:
            size = len(queue)
            ans += 1
            for _ in range(size):
                (row,col)  = queue.popleft(0)
                vr = [1, -1, 0, 0]
                vc = [0, 0, 1, -1]
                for i in range(4):
                    newRow = row + vr[i]
                    newCol = col + vc[i]
                    if 0 <= newRow < n and 0 <= newCol < m and grid[newRow][newCol] == 1:
                        grid[newRow][newCol]= 2
                        queue.append((newRow,newCol))
                        cnt -= 1
        return ans-1 if cnt == 0 else -1
                    

