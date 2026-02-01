class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        mp = dict()
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                slope = (points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                if slope in mp:
                    mp[slope] += 1
                else:
                    mp[slope] = 1
        