class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        n = len(grid)
        m = len(grid[0])
        ans = []
        for row in range(n-k+1):
            temp2 = []
            for col in range(m-k+1):
                temp = set()
                for i in range(row,row+k):
                    for j in range(col,col+k):
                        temp.add(grid[i][j])
                if len(temp) == 1:
                    temp2.append(0)
                else:
                    temp = list(temp)
                    temp.sort()
                    mini = float('inf')
                    for idx in range(1,len(temp)):
                        mini = min(mini,abs(temp[idx]-temp[idx-1]))
                    temp2.append(mini)
            ans.append(temp2)
        return ans
                

obj = Solution()
print(obj.minAbsDiff([[1,8],[3,-2]],2))