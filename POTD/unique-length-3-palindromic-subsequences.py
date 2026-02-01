import math
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        prefix = [[0]*26 for _ in range(n+1)]
        for i in range(n):
            for c in range(26):
                prefix[i+1][c] = prefix[i][c]
            prefix[i+1][ord(s[i])-ord('a')] += 1

        first = [-1]*26
        last = [-1]*26
        for idx,ch in enumerate(s):
            pos = ord(ch) - ord('a')
            if first[pos] ==  -1:
                first[pos] = idx
            last[pos] = idx
        
        for idx in range(26):
            start = first[idx]
            end = last[idx]
            if start == -1 or end - start > 2:
                continue
            for ch in range(26):
                if prefix[end][ch] - prefix[start+1][ch] > 0:
                    ans += 1
        return ans


obj = Solution()
print(obj.countPalindromicSubsequence("bbcbaba"))