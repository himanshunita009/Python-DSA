class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        power.sort()
        
        n = len(power)
        next_dp = [0]*(n+1)
        for idx in range(n-1,-1,-1):
            curr = [0]*(n+1)
            for prevIdx in range(-1,n):
                dp_prevIdx = prevIdx+1
                ans = next_dp[dp_prevIdx]
                if prevIdx == -1 or power[idx] == power[prevIdx] or power[idx] > power[prevIdx]+2:
                    ans = max(next_dp[idx+1]+power[idx],ans)
                curr[dp_prevIdx] = ans
            next_dp = curr
        return next_dp[0]
    
class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        power.sort()
        n = len(power)
        next_dp = [0]*(n+1)
        for idx in range(n-1,-1,-1):
            curr = [0]*(n+1)
            for prevIdx in range(-1,n):
                dp_prevIdx = prevIdx+1
                ans = next_dp[dp_prevIdx]
                if prevIdx == -1 or power[idx] == power[prevIdx] or power[idx] > power[prevIdx]+2:
                    ans = max(next_dp[idx+1]+power[idx],ans)
                curr[dp_prevIdx] = ans
            next_dp = curr.copy()
        return next_dp[0]

class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        power.sort()
        n = len(power)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for idx in range(n-1,-1,-1):
            for prevIdx in range(-1,n):
                dp_prevIdx = prevIdx+1
                ans = dp[idx+1][dp_prevIdx]
                if prevIdx == -1 or power[idx] == power[prevIdx] or power[idx] > power[prevIdx]+2:
                    ans = max(dp[idx+1][idx]+power[idx],ans)
                dp[idx][dp_prevIdx] = ans
        return dp[0][0]
    
class Solution:
    def __init__(self):
        self.freqMap = dict()
    def solve(self,power: list[int],idx: int,prevIdx: int,dp: dict):
        if idx == len(power):
            return 0
        ans = 0
        if (idx,prevIdx) in dp:
            return dp[(idx,prevIdx)]
        # Take
        if prevIdx == -1 or power[idx] == power[prevIdx] or power[idx] > power[prevIdx]+2:
            ans = self.solve(power,idx+self.freqMap[power[idx]],idx+self.freqMap[power[idx]]-1,dp)+(power[idx]*self.freqMap[power[idx]])
        ans = max(self.solve(power,idx+1,prevIdx,dp),ans)
        dp[(idx,prevIdx)] = ans
        return ans
    def maximumTotalDamage(self, power: list[int]) -> int:
        power.sort()
        dp = dict()
        freqMap = dict()
        for p in power:
            if p not in freqMap:
                freqMap[p] = 1
            else:
                freqMap[p] += 1
        self.freqMap = freqMap
        return self.solve(power,0,-1,dp)


class Solution:
    def solve(self,power: list[int],idx: int,prevIdx: int):
        if idx == len(power):
            return 0
        ans = 0
        # Take
        if prevIdx == -1 or power[idx] == power[prevIdx] or power[idx] > power[prevIdx]+2:
            ans = self.solve(power,idx+1,idx)+power[idx]
        ans = max(self.solve(power,idx+1,prevIdx),ans)
        return ans
    def maximumTotalDamage(self, power: list[int]) -> int:
        power.sort()
        return self.solve(power,0,-1)

obj = Solution()
print(obj.maximumTotalDamage([7,1,6,6]))