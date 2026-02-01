import math
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        flag = False
        for idx in range(1,len(nums)):
            if math.gcd(nums[idx],nums[idx-1]) == 1:
                flag = True
                break
        return len(nums) if flag else -1