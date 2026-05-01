class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = suffix = 1
        ans = 10**9
        for idx in range(n):
            prefix *= nums[idx]
            suffix *= nums[n-1-idx]
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            ans = max(ans,prefix*nums[idx],suffix*nums[n-1-idx])
        return ans
