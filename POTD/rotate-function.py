class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        temp = 0
        n = len(nums)
        for i in range(n):
            temp += (nums[i]*i)
        ans = temp
        prefix = [0]*n
        suffix = [0]*n
        for idx in range(1,n):
            prefix[idx] = prefix[idx-1]+nums[idx-1]
            suffix[n-1-idx] = suffix[n-idx]+nums[n-idx]
        i = n-1
        while i > 0:
            temp = temp + prefix[i] + suffix[i]  - (n-1)*nums[i]
            ans = max(ans,temp)
        return ans