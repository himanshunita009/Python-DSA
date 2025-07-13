class Solution:
    def __init__(self):
        self.dp = dict()
    def solve(self,idx,prev,k,events):
        if idx == len(events) or k == 0 :
            return 0
        if (idx,k,prev) in self.dp:
            return self.dp[(idx,k,prev)]
        notPick = self.solve(idx+1,k,prev,events)
        pick = 0
        if prev == -1 or (prev != -1 and events[prev][1] < events[idx][0]):
            pick = self.solve(idx+1,k-1,idx,events)+events[idx][2]
        self.dp[(idx,k,prev)] = max(pick,notPick)
        return self.dp[(idx,k,prev)]

    # def maxValue(self, events: list[list[int]], k: int) -> int:
    #     events.sort(key = lambda x:x[1])
    #     return self.solve(0,k,-1,events)
    def findNextDay(self,start_day,events):
        lo = start_day+1
        hi = len(events)-1
        ans = len(events)
        while lo <= hi:
            mid = (lo+hi)//2
            if events[mid][0] <= events[start_day][1]:
                lo = mid +1
            else:
                ans = mid
                hi = mid-1
        return ans
    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort(key = lambda x:x[0])
        n = len(events)
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        for idx in range(n-1,-1,-1):
            for j in range(1,k+1):
                dp[idx][j] = dp[idx+1][j]
                next_day = self.findNextDay(idx,events)
                dp[idx][j] = max(dp[idx][j],dp[next_day][j-1]+events[idx][2])
        return dp[0][k]