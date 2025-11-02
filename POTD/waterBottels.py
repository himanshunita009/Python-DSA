class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        sum = numBottles
        while numBottles > 0:
            temp = numBottles // numExchange
            sum += temp
            numBottles = temp + numBottles%numExchange
        return sum