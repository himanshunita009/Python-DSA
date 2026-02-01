from collections import defaultdict
class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        buildings.sort()
        xAxis = defaultdict(list)
        for x,y in buildings:
            xAxis[x].append(y)
        buildings.sort(key=lambda x: (x[1],x[0]))
        yAxis = defaultdict(list)
        for x,y in buildings:
            yAxis[y].append(x)
        ans = 0
        for x,y in buildings:
            xarr = xAxis[x]
            yarr = yAxis[y]
            if   xarr[0] < y < xarr[-1] and yarr[0] < x < yAxis[-1]:
                ans += 1
        return ans
        