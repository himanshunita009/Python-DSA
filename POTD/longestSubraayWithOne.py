class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        arr = []
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else :
                if cnt > 0:
                    arr.append(cnt)
                    cnt  =0
                arr.append(0)
        if cnt > 0 :
            arr.append(cnt)
        n = len(arr)
        ans = 0
        for i in range(n):
            if arr[i] == 0 :
                temp = 0
                if i > 0 and arr[i-1] > 0:
                    temp += arr[i-1]
                if i < n-1 and arr[i+1] > 0:
                    temp += arr[i+1]
                ans = max(ans,temp)
            else :
                ans = max(ans,arr[i]-1)
        return ans
    
obj = Solution()
print(obj.longestSubarray([1,1,1,1,1]))