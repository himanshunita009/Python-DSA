# class Solution:
#     def solve(self,i,endTiming, startTime: list[int], endTime: list[int], profit: list[int]):
#         if i >= len(startTime):
#             return 0
#         ans = 0
#         for k in range(i,len(startTime)):
#             if startTime[k] >= endTiming:
#                 ans = max(ans,self.solve(k+1,endTime[k],startTime,endTime,profit)+profit[k])
#         return ans
#     def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
#         jobs = sorted(zip(startTime, endTime, profit))
#         startTime, endTime, profit = zip(*jobs)
#         return self.solve(0,1,startTime,endTime,profit)

class Solution:
    def __init__(self):
        self.dp = dict()
        self.maxEndTime = 0
    def solve(self,i,endTiming, startTime: list[int], endTime: list[int], profit: list[int]):
        if i >= len(startTime):
            return 0
        if endTiming >= self.maxEndTime:
            return 0 
        if (i,endTiming) in self.dp:
            return self.dp.get((i,endTiming))
        ans = 0
        for k in range(i,len(startTime)):
            if startTime[k] >= endTiming:
                ans = max(ans,self.solve(k+1,endTime[k],startTime,endTime,profit)+profit[k])
            
        self.dp[(i,endTiming)] = ans 
        return self.dp.get((i,endTiming))
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        startTime, endTime, profit = zip(*jobs)
        for endTim in endTime:
            self.maxEndTime = max(self.maxEndTime,endTim)
        return self.solve(0,1,startTime,endTime,profit)