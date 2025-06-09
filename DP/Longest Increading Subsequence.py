class Solution:
    def solve(self,nums: list[int],ind: int,preIndex: int,dp: list[list[int]])-> int:
        if  ind == len(nums):
            return 0
        if dp[ind][preIndex+1] != -1:
            return dp[ind][preIndex+1]      
        pick = 0        
        if preIndex == -1 or nums[ind] > nums[preIndex]:
            pick = 1+self.solve(nums,ind+1,ind,dp)
    
        notPick = self.solve(nums,ind+1,preIndex,dp)
    
        dp[ind][preIndex+1] = max(pick,notPick)
        return dp[ind][preIndex+1]
    
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [[-1] * (len(nums)+1)]* len(nums)
        return self.solve(nums,0,-1,dp)

class Solution:
     def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [[0] * (n+1)]* (n+1)
        for ind in range(n-1,-1,-1):
            for prevInd in range(ind-1,-2,-1):
                pick = 0
                if prevInd == -1 or nums[ind] >  nums[prevInd]:
                    pick = 1+dp[ind+1][ind+1]
                notPick = dp[ind+1][prevInd+1]
                dp[ind][prevInd+1] = max(pick,notPick)
    
        return dp[0][0]