#User function Template for python3
class Solution:
    def solve(self,arr,ind,prev,dp):
        if ind == len(arr):
            return 0
        if dp[ind][prev] != -1:
            return dp[ind][prev]
        ans = self.solve(arr,ind+1,prev,dp)
        if prev == -1 or arr[ind] > arr[prev]:
            ans = max(ans,self.solve(arr,ind+1,ind,dp)+arr[ind])
        dp[ind][prev]= ans
        return dp[ind][prev]
    def maxSumIS(self, arr):
        dp = [[-1 for _ in range(len(arr)+1)] for _ in range(len(arr))]
        return self.solve(arr,0,-1,dp)