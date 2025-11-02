class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        mp = [[0]*(m-2) for _ in range(n-2)]
        for row in range(1,n-1):
            arr = heightMap[row]
            left = [-1]*m
            right = [-1]*m
            left[0] = arr[0]
            right[m-1] =arr[m-1]
            for i in range(1,m-1):
                left[i] = max(arr[i],left[i-1])
                right[m-1-i] = max(arr[m-1-i],right[m-i])
            for i in range(1,m-1):
                mini = min(left[i],right[i])
                if mini > arr[i]:
                   mp[row-1][i-1] = mini - arr[i]
        for col in range(1,m-1):
            top= [-1]*n
            bottom = [-1]*n
            top[0] = heightMap[0][1]
            bottom[n-1] = heightMap[n-1][1]
            for i in range(1,n-1):
                top[i] = max(top[i-1],heightMap[i][col])
                bottom[n-1-i] = max(bottom[n-i],heightMap[n-i-1][col])
            for i in range(1,n-1):
                mini = min(top[i],bottom[i])
                if mini > arr[i]:
                   mp[row-1][i-1] = mini - arr[i]
        ans = 0
        for row in mp:
            for val in row :
                ans += val
        return ans

obj = Solution()
print(obj.trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))
# print(obj.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))

