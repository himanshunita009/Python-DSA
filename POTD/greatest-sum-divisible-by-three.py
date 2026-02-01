from collections import defaultdict
class Solution:
    def __init__(self):
        self.dp = []
    def solve(self,idx, mod):
        if idx == len(self.dp):
            if mod == 0:
                return 0
            return float("-inf")

        if self.dp[idx][mod] != -1:
            return self.dp[idx][mod]

        pick = self.nums[idx] + self.solve(idx+1, (mod + self.nums[idx]) % 3)
        skip = self.solve(idx+1, mod)

        self.dp[idx][mod] = max(pick, skip)
        return self.dp[idx][mod]


    def maxSumDivThree(self, nums: list[int]) -> int:
        n = len(nums)
        self.dp = [[-1]*3 for _ in range(n)]
        self.nums = nums
        return self.solve(0,0)


obj = Solution()
print(obj.maxSumDivThree([3,6,5,1,8]))
