class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        n= len(stations)
        arr = [0]*n
        preSum = 0
        for i in range(r):
            preSum += stations[i]
        for i in range(r,n):
            preSum += stations[i]
            arr[i-r] = preSum
            preSum -= stations[i-r]
        preSum -= stations[n-r-1]
        for i in range(n-r,n):
            arr[i] = preSum
            preSum -= stations[i-r]

