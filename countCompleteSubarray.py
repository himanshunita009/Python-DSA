class Solution(object):
    def countCompleteSubarrays(self, nums):
        k = len(set(nums))
        mp = dict()
        ans = 0
        n = len(nums)
        i ,j = 0, 0

        while j < n:
            if len(mp) < k:
                if mp.get(nums[j]):
                    mp[nums[j]] += 1
                else:
                    mp[nums[j]] = 1
                j += 1
            if len(mp) == k:
                ans += (n-j+1)
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    mp.pop(nums[i])
                i += 1
        while i <= j and len(mp) == k:
            ans += (n-j+1)
            mp[nums[i]] -= 1
            if mp[nums[i]] == 0:
                mp.pop(nums[i])
            i += 1
        return ans

obj = Solution()
print(obj.countCompleteSubarrays([1,3,1,2,2]))