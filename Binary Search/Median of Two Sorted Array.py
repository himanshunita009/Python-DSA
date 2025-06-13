class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2,nums1)
        n = len(nums1)
        m = len(nums2)
        lo,hi = 0,n
        while lo <= hi:
            cut1 = (lo+hi)//2
            cut2 = (n+m+1)//2-cut1
            l1 = nums1[cut1-1] if cut1!=0 else -(10**6+10) 
            l2 = nums2[cut2-1] if cut2!=0 else -(10**6+10)
            r1 = nums1[cut1] if cut1!=n else 10**6+10
            r2 = nums2[cut2] if cut2!=n else 10**6+10
            if l1 <= r2 and l2<=r1 :
                if((n+m)%2 == 0):
                    return (max(l1,l2) + min(r1,r2))/2.0
                else:
                    return max(l1,l2)/1.0
            if l1 > r2:
                hi = cut1-1
            else:
                lo = cut1+1
        return 0.0
        