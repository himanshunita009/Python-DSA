class Solution:
    def countStableSubarrays(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        nxt = [0]*n
        nxt[-1] = n-1
        for idx in range(n-2,-1,-1):
            if nums[idx] <= nums[idx+1]:
                nxt[idx] = nxt[idx+1]
            else:
                nxt[idx] = idx
        ps_nxt = [0]*(n+1)
        for idx in range(n):
            length = nxt[idx]-idx+1
            ps_nxt[idx+1] = ps_nxt[idx]+length
        def solve(l: int,r: int):
            lo = l
            hi = r+1
            while lo < hi :
                mid = (lo+hi)//2
                if nxt[mid] > r:
                    hi = mid
                else:
                    lo = mid+1
            boundary = lo
            partA = 0
            if boundary > l:
                partA = ps_nxt[boundary]-ps_nxt[l]
            k = r - boundary+1
            partB = 0
            if k > 0:
                partB = (r+1)*k - (boundary*k + (k*(k-1)//2))
            return partA + partB
        ans = []
        for l,r in queries:
            ans.append(solve(l,r))
        return ans
obj = Solution()
print(obj.countStableSubarrays([19,5,22,4],[[2,3],[0,3]]))