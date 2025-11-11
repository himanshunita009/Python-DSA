class Solution:
    # m number of 0 
    # n number of 1 
    def __init__(self):
        self.dp = dict()
    def solve(self,idx: int,m: int,n: int,mp: dict,N: int):
        if idx == N:
            return 0
        if (idx,m,n) in self.dp:
            return self.dp[(idx,m,n)]
        subsets = self.solve(idx+1,m,n,mp,N)
        if mp[idx][0] <= m and mp[idx][1] <= n:
            subsets = max(subsets,self.solve(idx+1,m-mp[idx][0],n-mp[idx][1],mp,N)+1)
        self.dp[(idx,m,n)] = subsets
        return self.dp[(idx,m,n)]
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        mp = dict()
        for idx in range(len(strs)):
            zeros = 0
            once = 0
            for ch in strs[idx]:
                if ch == '0':
                    zeros += 1
                else:
                    once += 1
            mp[idx] = [zeros,once]
        return self.solve(0,m,n,mp,len(strs))