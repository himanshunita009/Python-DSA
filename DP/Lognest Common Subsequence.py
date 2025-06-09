# class Solution:
#     def solve(self,text1,text2,i,j,dp):
#         if i < 0 or j < 0:
#             return 0
#         if dp[i][j] != -1:
#             return dp[i][j]
#         if text1[i] == text2[j]:
#             dp[i][j] = self.solve(text1,text2,i-1,j-1,dp)+1
#         else:
#             dp[i][j] = max(self.solve(text1,text2,i,j-1,dp),self.solve(text1,text2,i-1,j,dp))
#         return dp[i][j]

#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
#         return self.solve(text1,text2,len(text1)-1,len(text2)-1,dp)
    

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        return dp[n][m]
    