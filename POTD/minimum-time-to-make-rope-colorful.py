class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        n = len(colors)
        ans = 0
        for idx in range(1,n):
            if colors[idx] == colors[idx-1]:
                ans += min(neededTime[idx],neededTime[idx-1])
                if neededTime[idx] < neededTime[idx-1]:
                    neededTime[idx] , neededTime[idx-1] = neededTime[idx-1], neededTime[idx]
        return ans 