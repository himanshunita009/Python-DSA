import math
class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        n =len(grid)
        m =len(grid[0])
        tSum = 0
        for row in grid:
            tSum += sum(row)
        avg1 = math.ceil(tSum/(n*m))
        avg2 = avg1-1
        ans1 = 0
        ans2 = 0
        for row in range(n):
            for col in range(m):
                abs1 = abs(avg1-grid[row][col])
                if abs1%x == 0:
                    ans1 += (abs1//x)
                abs2 = abs(avg2-grid[row][col])
                if abs2%x == 0:
                    ans2 += (abs2//x)
        return min(ans1,ans2)

obj= Solution()
print(obj.minOperations([[2,4],[6,8]],2))