class Solution(object):
    def numSubseq(self, nums, target):
        n = len(nums)
        dp = [[{"cnt": 0,"min": float("inf"),"max": float("-inf")}] * (target+1) for _ in range(n+1)]
        dp[0][0]["cnt"] = 1

        for idx in range(1,n+1):
            for tsum in range(0,target+1):
                tmin = min(dp[idx-1][tsum]["min"],nums[idx-1])
                tmax = max(dp[idx-1][tsum]["max"],nums[idx-1])
                dp[idx][tsum] = dp[idx-1][tsum]
                temp = tmin + tmax
                if temp <= tsum:
                    dp[idx][tsum] = {
                        "cnt": dp[idx][tsum]["cnt"]+dp[idx-1][temp]["cnt"],
                        "min" : tmin,
                        "max" : tmax
                    }
        return dp[n][target]["cnt"] 
obj = Solution()    
print(obj.numSubseq([3,5,6,7],9))