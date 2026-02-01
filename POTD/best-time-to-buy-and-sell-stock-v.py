class Solution:
    def solve(self,idx: int,buySell: int,prices: list[int],k: int):
        if idx == len(prices) or k == 0:
            if buySell == -1:
                return 0
            else:
                return float('-inf')
        if (idx,buySell,k) in self.dp:
            return self.dp.get((idx,buySell,k)) 
        if buySell == -1:
            self.dp[(idx,buySell,k)] = max(
                self.solve(idx+1,buySell,prices,k),
                self.solve(idx+1,1,prices,k)-prices[idx],
                self.solve(idx+1,2,prices,k)+prices[idx],
            )
        if buySell == 1:
            self.dp[(idx,buySell,k)] = max(
                self.solve(idx+1,-1,prices,k-1)+prices[idx],
                self.solve(idx+1,buySell,prices,k)
            )
        self.dp[(idx,buySell,k)] = max(
            self.solve(idx+1,-1,prices,k-1)-prices[idx],
            self.solve(idx+1,buySell,prices,k)
        )
        return self.dp[(idx,buySell,k)]
    def maximumProfit(self, prices: list[int], k: int) -> int:
        self.dp = dict()
        return self.solve(0,-1,-1,prices,k)