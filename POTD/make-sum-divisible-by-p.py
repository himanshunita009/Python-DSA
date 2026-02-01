class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        totalSum = sum(nums)
        rem = totalSum%p
        if rem == 0:
            return 0
        n = len(nums)
        mp = dict()
        mp[0] = -1
        ans = n
        prefixSum = 0
        for idx in range(n):
            prefixSum = (prefixSum+nums[idx])%p
            if (prefixSum+p-rem)%p in mp:
                ans = min(ans,idx-mp[(prefixSum+p-rem)%p])
            mp[prefixSum] = idx
        return -1 if ans == n else ans
obj = Solution()
print(obj.minSubarray([8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2],148))