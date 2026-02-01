class Solution:
    def sumAndMultiply(self, s: str,queries: list[list[int]]) -> list[int]:
        mod = 10**9+7
        n = len(s)
        tempSum = 0
        num =0
        prefix = list()
        prefix = [[0,0,0] for _ in range(n+1)]
        k = 0
        for ch in s:
            if ch != '0':
                k += 1
        for idx in range(n):
            if s[idx] != '0':
                temp = int(s[idx])
                tempSum = int(s[idx])
                prefix[idx+1] = [(prefix[idx][0]*10+temp)%mod,(prefix[idx][1]+tempSum)%mod,k] 
                k -= 1
            else:
                prefix[idx+1] = prefix[idx]
        ans = list()
        for l,r in queries:
            tempNum = prefix[r+1][0]- int(prefix[l][0]*(10**(prefix[l][2]-prefix[r+1][2])))
            tempSum = prefix[r+1][1]- prefix[l][1]
            
            ans.append((tempNum*tempSum)%mod)

        return ans
        # n = 0
        # while num > 0:
        #     n = n*10+num%10
        #     num //= 10
        # return sum * n

obj = Solution()
print(obj.sumAndMultiply("10203004",[[0,7],[1,3],[4,6]]))