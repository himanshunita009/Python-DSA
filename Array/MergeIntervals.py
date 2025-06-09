class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(m-n):
            if nums1[i] >  nums2[0]:
                nums1[i], nums2[0] = nums2[0],nums1[i]
        for i in range(m-n,m):
            nums1[i] = nums2[i-m+n]
        

