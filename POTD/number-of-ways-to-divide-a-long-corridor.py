class Solution:
    def numberOfWays(self, corridor: str) -> int:
        totalSeats = corridor.count("S")
        n = len(corridor)
        if totalSeats == 2:
            return 1
        if totalSeats <= 1:
            return 0
        segments = []
        mod = 10**9+7
        start= -1
        for idx in range(n):
            if corridor[idx] == "S":
                if start == -1:
                    start =end = idx
                else:
                    segments.append((start,idx))
                    start = -1
        ans = 0
        for idx in range(1,len(segments)):
            prevEnd = segments[idx-1][1]
            currStart,currEnd = segments[idx]
            ans += (currStart-prevEnd)
        return ans       

obj = Solution()
print(obj.numberOfWays("SPPSSSPPSPPS"))