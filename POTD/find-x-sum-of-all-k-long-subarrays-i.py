class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        mp = dict()
        n = len(nums)
        ans = []
        for idx in range(n):
            num = nums[idx]
            if num not in mp:
                mp[num] = 1
            else:
                mp[num] += 1
            if idx+1 > k:
                mp[nums[idx-k]] -= 1
                if mp[nums[idx-k]] == 0:
                    mp.pop(nums[idx-k])
            if idx+1 >= k:
                xsum = list(mp.items())
                xsum.sort(key=lambda x: (x[1],x[0]))
                temp = 0
                for idx in range(len(xsum)-1,len(xsum)-x-1,-1):
                    temp += (xsum[idx][0]*xsum[idx][1])
                ans.append(temp)
        return ans
obj = Solution()
print(obj.findXSum([9,2,2],3,3))
            