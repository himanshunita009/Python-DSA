class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = float("-inf")
        prefix = [0]*(n+1)
        for i in range(1,n+1):
            prefix[i] = prefix[i-1]+nums[i-1]
        for i in range(1,k+1):
            endIdx = i+k-1
            tempAns = float("-inf")
            currSum = 0
            startIdx = i
            while endIdx <=n and (endIdx-startIdx+1)%k == 0:
                currSum += (prefix[endIdx]-prefix[startIdx-1])
                tempAns = max(tempAns,currSum)
                if currSum < 0:
                    currSum = 0
                endIdx += k
                startIdx += k
            ans = max(ans,tempAns)
        return ans
            
obj = Solution()
print(obj.maxSubarraySum([-1,2,4],1))