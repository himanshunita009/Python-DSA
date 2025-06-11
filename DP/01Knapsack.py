
class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]):
        n = len(val)
        dp  = [[0 for _ in range(W+1)] for _ in range(n)]
        for i in range(wt[0],W+1):
            dp[0][i] = val[0]

        for i in range(1,n):
            for j in range(W+1):
                dp[i][j] = dp[i-1][j]
                if j >= wt[i]:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-wt[i]]+val[i])
        return dp[n-1][W]

class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]):
        n = len(val)
        prev  = [0 for _ in range(W+1)]
        curr  = [0 for _ in range(W+1)]
        for i in range(wt[0],W+1):
            prev[i] = val[0]

        for i in range(1,n):
            for j in range(W+1):
                curr[j] = prev[j]
                if j >= wt[i]:
                    curr[j] = max(curr[j],prev[j-wt[i]]+val[i])
            prev = curr.copy()
        return curr[W]

class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]):
        n = len(val)
        prev  = [0 for _ in range(W+1)]
        for i in range(wt[0],W+1):
            prev[i] = val[0]

        for i in range(1,n):
            for j in range(W+1,-1,-1):
                prev[j] = 0 + prev[j] # Not pick case
                if j >= wt[i]:
                    prev[j] = max(prev[j],prev[j-wt[i]]+val[i])
        return prev[W]
