class Solution:
    def solve(self,start,end,cuts):
        if start+1 >= end:
            return 0
        ans = float('inf')
        for k in range(start+1,end):
            ans = min(ans,self.solve(start,k,cuts)+self.solve(k,end,cuts)+cuts[end]-cuts[start])
        return 0 if ans == float('inf') else ans
    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts = [0] + sorted(cuts)+[n]
        ans = self.solve(0,len(cuts)-1,cuts)
        return ans

class Solution:
    def solve(self,start,end,cuts,dp):
        if start+1 >= end:
            return 0
        ans = float('inf')
        if dp[start][end] != -1:
            return dp[start][end]
        for k in range(start+1,end):
            ans = min(ans,self.solve(start,k,cuts,dp)+self.solve(k,end,cuts,dp)+cuts[end]-cuts[start])
        dp[start][end] = 0 if ans == float('inf') else ans
        return dp[start][end]
    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts = [0] + sorted(cuts)+[n]
        m = len(cuts)
        dp = [[-1 for _ in range(m)] for _ in range(m)]
        ans = self.solve(0,len(cuts)-1,cuts,dp)
        return ans

class Solution:
    def solve(self,start,end,cuts,dp):
        if start+1 >= end:
            return 0
        ans = float('inf')
        if dp[start][end] != -1:
            return dp[start][end]
        for k in range(start+1,end):
            ans = min(ans,self.solve(start,k,cuts,dp)+self.solve(k,end,cuts,dp)+cuts[end]-cuts[start])
        dp[start][end] = 0 if ans == float('inf') else ans
        return dp[start][end]
    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts = [0] + sorted(cuts)+[n]
        m = len(cuts)
        dp = [[-1 for _ in range(m)] for _ in range(m)]
        for start in range(m):
            for end in range(m):
                if start+1 >= end:
                    dp[start][end] = 0
        for start in range(m):
            for end in range(m):
                ans = float('inf')
                for k in range(start+1,end):
                    ans = min(ans,dp[start][k]+dp[k][end]+cuts[end]-cuts[start])
                dp[start][end] = 0 if ans == float('inf') else ans
        
        return dp[start][end]


