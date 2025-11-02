class Solution:
    def sortVowels(self, s: str) -> str:
        arr = ['A','E','I','O','U','a','e','i','o','u']
        fq = [0]*10

        for ch in s :
            if ch in arr :
                fq[arr.index(ch)] += 1

        j = 0
        ans = ""
        i = 0
        while i < len(arr) and fq[i]  == 0:
            i += 1
        while j < len(s) and i < len(arr):
            if s[j] in arr:
                ans += arr[i]
                fq[i] -= 1
                while i < len(arr) and fq[i] == 0:
                    i += 1
            else:
                ans += s[j]
            j += 1
        if j < len(s):
            ans += s[j:]

        return ans
    
obj= Solution()
print(obj.sortVowels("lYmpH"))
                