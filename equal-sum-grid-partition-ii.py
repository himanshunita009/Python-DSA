from collections import defaultdict
class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        rSum = [0]*n
        cSum = [0]*m
        for row in range(n):
            for col in range(m):
                rSum[row] += grid[row][col]
                cSum[col] += grid[row][col]
            if row > 0:
                rSum[row] += rSum[row-1]
        if rSum[n-1]&1:
            return False
        for col in range(1,m):
            cSum[col] += cSum[col-1]
        targetSum = rSum[n-1]//2
        if rSum.count(targetSum) != 0 or cSum.count(targetSum) != 0:
            return True
        
        for row in range(n):
            for col in range(m):
                ele = grid[row][col]
                if row != n-1 and rSum[row] - ele == rSum[n-1]-rSum[row]:
                    if row == 0 :
                        if col == 0 or col == m-1:
                            return True
                        else:
                            continue
                    else:
                        return True
                if row != 0 and rSum[n-1]-rSum[row-1] - ele == rSum[row-1]:
                    if row == n-1:
                        if col == 0 or col == m-1:
                            return True
                        else:
                            continue
                    else:
                        return True
                if col != m-1 and cSum[col] - ele == targetSum :
                    if col == 0:
                        if row == 0 or row == n-1:
                            return True
                        else:
                            continue
                    else:
                        return True
                if col != 0 and cSum[m-1]-cSum[col-1] - ele == targetSum:
                    if col == m-1:
                        if row == 0 or row == n-1:
                            return True
                        else:
                            continue
                    else:
                        return True
        return False
                
obj = Solution()
print(obj.canPartitionGrid([[5,5,6,2,2,2]]))