class Solution:
    def findPages(self, arr, k):
        n = len(arr)
        if k > n :
            return -1
        hi = 0
        lo = 10**3+10
        ans = 10**3+10
        for ele in arr:
            sum += ele
            lo = min(lo,ele)
        while lo <= hi:
            mid = (lo+hi)//2
            tSum = 0
            count = 1
            for ele in arr:
                tSum += ele
                if tSum > mid:
                    tSum = ele
                    count += 1
            if count > k :
                lo = mid + 1
            else:
                hi = mid-1
                ans = ans
        return ans

