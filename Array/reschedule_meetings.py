class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        ans = 0
        prevEnd = 0
        n = len(startTime)
        for i in range(n):
            startTime[i] = startTime[i] - prevEnd
            prevEnd = endTime[i]
        startTime.append(eventTime - prevEnd)
        sum = 0
        k = k+1
        for i in range(n+1):
            sum += startTime[i]
            if (i+1) >= k:
                if (i+1) > k:
                    sum -= startTime[i-k]
                ans = max(ans,sum)
        return ans

obj = Solution()
print(obj.maxFreeTime(10,1,[0,2,9],[1,4,10]))