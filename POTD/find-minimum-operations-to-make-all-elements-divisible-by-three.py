class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans += (num%3)
        return ans
