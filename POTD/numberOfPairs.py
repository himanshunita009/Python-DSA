class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        points.sort()
        cnt = 0
        for i in range(1,len(points)):
            if points[i-1][1] >= points[i][1]:
                cnt += 1
        return cnt

obj = Solution()
print(obj.numberOfPairs([[0,1],[1,3],[6,1]]))