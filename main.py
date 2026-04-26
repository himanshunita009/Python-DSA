class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        if grid[0][0] > k:
            return 0
        n = len(grid)+1
        m = len(grid[0])
        ans = 0
        grid.insert(0,[0]*m)
        for row in range(1,n):
            grid[row][0] += grid[row-1][0]
            if grid[row][0] <= k:
                ans += 1
                # grid[row][0]
            else:
                break
            for col in range(1,m):
                grid[row][col] = grid[row][col-1]+grid[row-1][col] - grid[row-1][col-1]
                if grid[row][col] <= k:
                    ans += 1 
        return ans
obj = Solution()
print(obj.countSubmatrices([[7,6,3],[6,6,1]],18))
