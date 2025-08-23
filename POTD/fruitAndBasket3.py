class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        temp = []
        for idx,value in enumerate(baskets):
            temp.append((value,idx))
        temp.sort(key=lambda x : x[0])
        n = len(fruits)
        for idx in range(n):
            fruit = fruits[idx]
            lo = 0
            hi = n-1
            tempIdx = -1
            while lo<=hi:
                mid = (lo+hi)//2
                if temp[mid][0] >= fruit:
                    tempIdx = mid
                    hi = mid-1
                else:
                    lo = mid+1
            

            