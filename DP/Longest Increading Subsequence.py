# class Solution:
#     def solve(self,nums: list[int],ind: int,preIndex: int,dp: list[list[int]])-> int:
#         if  ind == len(nums):
#             return 0
#         if dp[ind][preIndex+1] != -1:
#             return dp[ind][preIndex+1]      
#         pick = 0        
#         if preIndex == -1 or nums[ind] > nums[preIndex]:
#             pick = 1+self.solve(nums,ind+1,ind,dp)
    
#         notPick = self.solve(nums,ind+1,preIndex,dp)
    
#         dp[ind][preIndex+1] = max(pick,notPick)
#         return dp[ind][preIndex+1]
    
#     def lengthOfLIS(self, nums: list[int]) -> int:
#         dp = [[-1] * (len(nums)+1)]* len(nums)
#         return self.solve(nums,0,-1,dp)

class Solution:
    def solve(self, word1: str,i :int, word2: str,j: int,dp):
        if i <= 0:
            return j +1 
        if j <= 0:
            return i+1
        if dp[i][j] != -1:
            return dp[i][j]
        if word1[i] == word2[j]:
            return self.solve(word1,i-1,word2,j-1,dp)
        ans = self.solve(word1,i-1,word2,j,dp)+1
        ans = min(ans,self.solve(word1,i,word2,j-1,dp)+1)
        ans = min(ans,self.solve(word1,i-1,word2,j-1,dp)+1)
        dp[i][j] = ans
        return dp[i][j]

    def minDistance(self, word1: str, word2: str) -> int:
        n = len (word1)
        m = len (word2)
        if n == 0:
            return m
        if m == 0:
            return n 
        dp = [[-1 for _ in range(m)] for _ in range(n) ]
        return self.solve(word1,n-1,word2,m-1,dp)
    
obj = Solution()
print(obj.minDistance("a","a"))