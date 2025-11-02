class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = set()
        i = 0
        j = 0
        ans = 0
        while j < len(s):
            if s[j] in mp:
                while i < j and s[j] in mp:
                    mp.remove(s[i])
                    i+= 1
            mp.add(s[j])
            ans = max(ans,len(mp))
            j += 1
        return ans 
