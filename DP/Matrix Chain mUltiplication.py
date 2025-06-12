class Solution:
    def solve(self,arr,i,j):
        if i >= j:
            return 0
        ans = 20**9
        for k in range(i,j):
            temp = self.solve(arr,i,k) + self.solve(arr,k+1,j) + arr[i-1]* arr[k] * arr[j]
            ans = min(ans,temp)
        return ans
    def matrixMultiplication(self, arr):
        return self.solve(arr,1,len(arr)-1)
class Solution:
    def solve(self,arr,i,j,dp):
        if dp[i][j] != -1:
            return dp[i][j]
        ans = 20**9
        for k in range(i,j):
            temp = self.solve(arr,i,k) + self.solve(arr,k+1,j) + arr[i-1]* arr[k] * arr[j]
            ans = min(ans,temp)
        return ans
    def matrixMultiplication(self, arr):
        n = len(arr)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i >= j :
                    dp[i][j] = 0
        return self.solve(arr,1,len(arr)-1,dp)
    
class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i >= j :
                    dp[i][j] = 0
        return self.solve(arr,1,len(arr)-1,dp)
    