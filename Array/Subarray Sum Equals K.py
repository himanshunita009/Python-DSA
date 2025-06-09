class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = dict()
        sum  = 0
        mp[0] = 1
        ans = 0
        for num in nums:
            sum += num
            if mp.get(sum-k) is not None:
                ans += mp[sum-k]
            mp[sum] = mp[sum]+1 if mp.get(sum) is not None else 1 
        return ans