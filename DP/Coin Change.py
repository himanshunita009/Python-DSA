class Solution:
    def __init__(self):
        self.target = 0
        self.maxi = 10**9
    def solve(self,i,sum,coins):
        if sum == 0:
            return 0
        if i == 0:
            return self.maxi if sum != 0 else 0
        len = self.solve(i-1,sum,coins)
        
        min = self.solve(i,sum-coins[i],coins)

        
    def coinChange(self, coins: list[int], amount: int) -> int:
        self.target = amount
        

class Solution:
    def __init__(self):
        self.maxi = float('inf')
    def solve(self,i: int, sum: int , coins: list[int]):
        if i < 0 or sum <= 0:
            return 0 if sum == 0 else self.maxi
        res = self.solve(i-1,sum,coins)
        if coins[i] <= sum:
            res = min(res,1+self.solve(i,sum-coins[i],coins))
        return res
        
    def coinChange(self, coins: list[int], amount: int) -> int:
        ans = self.solve(len(coins)-1,amount,coins) 
        return -1 if ans == self.maxi else ans

class Solution:
    def __init__(self):
        self.maxi = float('inf')
    def solve(self,i: int, sum: int , coins: list[int],dp):
        if i < 0 or sum <= 0:
            return 0 if sum == 0 else self.maxi
        if dp[i][sum] != -1:
            return dp[i][sum]
        res = self.solve(i-1,sum,coins,dp)
        if coins[i] <= sum:
            res = min(res,1+self.solve(i,sum-coins[i],coins,dp))
        dp[i][sum] = res
        return dp[i][sum]
        
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [[ -1 for _ in range(amount+1)] for _ in range(len(coins))]
        ans = self.solve(len(coins)-1,amount,coins,dp)
        return -1 if ans == self.maxi else ans

class Solution:
    def __init__(self):
        self.maxi = float('inf')
    def solve(self,i: int, sum: int , coins: list[int],dp):
        if i < 0 or sum <= 0:
            return 0 if sum == 0 else self.maxi
        if dp[i][sum] != -1:
            return dp[i][sum]
        res = self.solve(i-1,sum,coins,dp)
        if coins[i] <= sum:
            res = min(res,1+self.solve(i,sum-coins[i],coins,dp))
        dp[i][sum] = res
        return dp[i][sum]
        
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        dp = [[ -1 for _ in range(amount+1)] for _ in range(n+1)]
        for j in range(amount+1):
            dp[0][j] = self.maxi
        for i in range(1,n+1):
            dp[i][0] = 0
        for i in range(1,n+1):
            for j in range(1,amount+1):
                res = dp[i-1][j]
                if coins[i-1] <= j:
                    res = min(res,1+dp[i][j-coins[i-1]])
                dp[i][j] = res

        return -1 if dp[n][sum] == self.maxi else dp[n][sum]