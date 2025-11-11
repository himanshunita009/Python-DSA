from collections import deque

class Solution:
    def findCost(self, credit: int, k: int):
        if credit == 0:
            return k
        elif credit == 1:
            return k - 1
        else: 
            return k - 1

    def maxPathScore(self, grid: list[list[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        score = [[-1] * m for _ in range(n)]
        queue = deque([(0, 0, 0, k)]) 
        quantelis = (grid, k, n, m)

        while queue:
            row, col, prevScore, tempK = queue.popleft()
            if tempK < 0:
                continue
            newScore = prevScore + grid[row][col]
            newK = self.findCost(grid[row][col], tempK)
            if newK >= 0 and newScore > score[row][col]:
                score[row][col] = newScore
                directions = [(1, 0), (0, 1)]
                for dx, dy in directions:
                    newRow, newCol = row + dx, col + dy
                    if 0 <= newRow < n and 0 <= newCol < m:
                        queue.append((newRow, newCol, newScore, newK))
        return score[n - 1][m - 1] if score[n - 1][m - 1] != -1 else -1
