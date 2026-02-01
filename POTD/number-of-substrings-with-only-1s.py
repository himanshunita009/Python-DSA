class Solution:
    def numSub(self, s: str) -> int:
        n = len(s)
        cnt = 0
        ans = 0
        mod = 10**9+7
        for ch in s:
            if ch == '1':
                cnt += 1
            else:
                ans = ((ans)%mod + (cnt*(cnt+1)//2)%mod)%mod
                cnt = 0
        if cnt > 1:
            print("Hi")
            ans = ((ans)%mod + (cnt*(cnt+1)//2)%mod)%mod
        return ans

obj = Solution()
print(obj.numSub("101"))