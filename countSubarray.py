class Solution(object):
    def rightTrim(self,mp,nums,arr):
        for i in range(len(nums)-1,-1,-1):
            if mp[nums[i]] == 1: 
                break
            else :
                arr = arr[:-1]
                mp[nums[i]] -= 1
        return arr
    
    def leftTrim(self,mp,nums,arr):
        for i in range(len(nums)):
            if mp[nums[i]] == 1: 
                break
            else :
                arr = arr[1:]
                mp[nums[i]] -= 1
        return arr

    def calculateAns(self,s,n):
        diff = n-s
        return diff + 2 - (1 if diff == 1 else 0)

    def compareArray(self,nums1,nums2):
        if len(nums1) != len(nums2):
            return False
        for i in range(len(nums1)):
            if nums1[i] != nums2[i]:
                return False
        return True

    def countCompleteSubarrays(self,arr):
        mp = dict()
        n = len(arr)
        for num in arr:
            if mp.get(num):
                mp[num] += 1
            else:
                mp[num] = 1
        if len(mp) == 1:
            return (n*(n+1)//2)
        tempMp = mp.copy()
        # 1st attempt
        brr = arr
        crr = arr
        brr = self.rightTrim(mp,arr,brr)
        brr = self.leftTrim(mp,arr,brr)
        
        # 2nd attempt
        crr = self.leftTrim(tempMp,arr,crr)
        crr = self.rightTrim(tempMp,arr,crr)
        
        if(self.compareArray(brr,crr)):
            return self.calculateAns(len(brr),n)
        else:
            return self.calculateAns(len(brr),n) + self.calculateAns(len(crr),n) - 1
            
obj = Solution()
print(obj.countCompleteSubarrays([1917,1917,608,608,1313,751,558,1561,608]))