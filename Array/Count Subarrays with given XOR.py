class Solution:
    def subarrayXor(self, arr, k):
        prefixXor = 0
        mp = dict()
        mp[prefixXor] = 1
        ans = 0
        for num in arr:
            prefixXor ^= num
            if prefixXor^k in mp:
                ans += mp.get(prefixXor^k)
            if prefixXor in mp:
                mp[prefixXor] += 1
            else:
                mp[prefixXor] = 1
        return ans
obj = Solution()
print(obj.subarrayXor([4, 2, 2, 6, 4],6))
    