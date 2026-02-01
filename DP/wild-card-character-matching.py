class Solution:
    def solve(self,idx1: int,idx2: int):
        if idx1 == len(self.s) and idx2 == len(self.p):
            return True
        if idx2 == len(self.p):
            return False
        if idx1 == len(self.s):
            return self.p[idx2] == '*' and self.solve(idx1,idx2+1)
        if self.s[idx1] == self.p[idx2] or self.p[idx2] == '?':
            return self.solve(idx1+1,idx2+1)
        if self.p[idx2] == '*':
            return max(self.solve(idx1+1,idx2),self.solve(idx1,idx2+1)) 
        else:
            return False
    # def isMatch(self, s: str, p: str) -> bool:
    #     self.s = s
    #     self.p = p
        # return self.solve(0,0)
    # def isMatch(self, s: str, p: str) -> bool:
    #     n = len(s)    
    #     m = len(p)
    #     dp = [[False]*(m+1) for _ in range(n+1)]
    #     dp[0][0] = True
    #     for i in range(1,m+1):
    #         if p[i-1] == '*':
    #             dp[0][i] = dp[0][i-1]
    #     for i in range(1,n+1):
    #         for j in range(1,j+1):
    #             if s[i-1] == p[j-1] or p[j-1] == '*':
    #                 dp[i][j] = dp[i-1][j-1]
    #             if p[j-1] == '*':
    #                 dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    #             else:
    #                 dp[i][j] = False
    #     return dp[n][m]
    def isMatch(self,s: str,p: str) -> str:
        startIdx = -1
        match = -1
        i =j = 0
        n = len(s)
        m = len(p)
        while i < n:
            if j < m and s[i] == p[j] or p[j] == '?':
                i += 1 
                j += 1
            elif j < m and p[j] == '*':
                startIdx = j
                match = i
                j += 1
            elif startIdx != -1:
                j = startIdx +1 
                match += 1
                i = match
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        return  j == m




