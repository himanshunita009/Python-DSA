class Solution:
    def solve(self, word1: str,i :int, word2: str,j: int):
        if i == 0:
            return j +1 
        if j == 0:
            return i+1
        if word1[i] == word2[j]:
            return self.solve(word1,i-1,word2,j-1)
        ans = self.solve(word1,i-1,word2,j)+1
        ans = min(ans,self.solve(word1,i,word2,j-1)+1)
        ans = min(ans,self.solve(word1,i-1,word2,j-1)+1)
        return ans

    def minDistance(self, word1: str, word2: str) -> int:
        return self.solve(word1,len(word1)-1,word2,len(word2)-1)

class Solution:
    def solve(self, word1: str,i :int, word2: str,j: int,dp):
        if i == 0:
            return j +1 
        if j == 0:
            return i+1
        if dp[i][j] != -1:
            return dp[i][j]
        if word1[i] == word2[j]:
            return self.solve(word1,i-1,word2,j-1)
        ans = self.solve(word1,i-1,word2,j,dp)+1
        ans = min(ans,self.solve(word1,i,word2,j-1,dp)+1)
        ans = min(ans,self.solve(word1,i-1,word2,j-1,dp)+1)
        dp[i][j] = ans
        return dp[i][j]

    def minDistance(self, word1: str, word2: str) -> int:
        n = len (word1)
        m = len (word2)
        dp = [[-1] for _ in range(m) for _ in range(n) ]
        return self.solve(word1,n-1,word2,m-1,dp)