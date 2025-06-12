class Solution:
    def solve(self,start,end,cuts):
        if start >= end-1:
            return 0
        ans = float('inf')
        for cut in cuts:
            if start <= cut <= end:
                ans = min(ans,self.solve(start,cut-1,cuts)+self.solve(cut+1,end,cuts)+end-start)
        return ans
    def minCost(self, n: int, cuts: list[int]) -> int:
        return self.solve(0,n,cuts)