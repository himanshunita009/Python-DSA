from math import sqrt
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for l in range(n):
            ones =0
            zeros = 0
            r = l 
            while r < n and zeros <= int(sqrt(n)):
                if s[r] == '0':
                    zeros += 1
                else:
                    ones += 1
                if ones >= zeros**2:
                    ans += 1
                r += 1
        return ans


obj = Solution()
print(obj.numberOfSubstrings("101101"))