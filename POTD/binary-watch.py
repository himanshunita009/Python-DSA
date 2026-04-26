from collections import defaultdict
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        hoursMap = defaultdict(list)
        minsMap = defaultdict(list)
        for hour in range(13):
            temp = hour
            setBitCount = 0
            while temp > 0:
                if temp&1:
                    setBitCount += 1
                temp = temp >> 1
            hoursMap[setBitCount].append(hour)
        for mins in range(60):
            temp = mins
            setBitCount = 0
            while temp > 0:
                if temp&1:
                    setBitCount += 1
                temp = temp >> 1
            minsMap[setBitCount].append(mins)
        ans = list()
        temp = defaultdict(list)
        for hourBitCount in range(turnedOn+1):
            minsBitCount = turnedOn-hourBitCount
            possibleHours = hoursMap[hourBitCount]
            possibleMins = minsMap[minsBitCount]
            for hour in possibleHours:
                for mins in possibleMins:
                    time = str(hour)+":"+str(mins).zfill(2)
                    temp[hour].append(time)
        for hour in range(13):
            if hour in temp:
                ans += temp[hour]
        return ans
    
obj = Solution()
print(obj.readBinaryWatch(5))