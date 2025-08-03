class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        ycount = dict()
        mod = 10**9+7
        for point in points:
            _,y = point
            if y in ycount:
                ycount[y] += 1
            else :
                ycount[y] = 1
        if len(ycount) <= 1:
            return 0
        ans = 0
        temp = []
        for val in ycount.values():
            if val > 1:
                temp.append(val*(val-1)//2)
        if len(temp) <= 1:
            return 0
        t = len(temp)
        prefixSum = [0 for _ in range(t)]
        prefixSum[t-1] = temp[t-1]
        for i in range(len(temp)-2,-1,-1):
            prefixSum[i] = prefixSum[i+1]+temp[i]
        for i in range(t-1):
            ans += (prefixSum[i+1]*temp[i])
        return ans
if __name__ == "__main__":
    obj = Solution()
    temp = [[[1,0],[2,0],[3,0],[2,2],[3,2]],
            [[0,0],[1,0],[0,1],[2,1]],
            [[54,91],[-37,91],[-6,91],[-33,91]],
            [[50,-41],[64,-66],[-45,-41],[-58,10],[25,10]],
            [[87,-39],[12,-94],[-30,-11],[-76,-11]],
            [[-73,-72],[-1,-56],[-92,30],[-57,-89],[-19,-89],[-35,30],[64,-72]]]
    for q in temp:
        print(obj.countTrapezoids(q))