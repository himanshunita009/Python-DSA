class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        sum = 0
        mp = {0:-1}
        for i,num in enumerate(nums):
            sum = (sum+num)%k
            if sum in mp and i-mp[sum] > 1:
                return True
            else:
                mp[sum] = i
        return False
