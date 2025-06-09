class Solution():
    def findLPS(self,text):
        i=0
        j=1
        lps = [0]*len(text)
        while j < len(text):
            if text[i] == text[j]:
                lps[j] = i+1
                i += 1
                j += 1
            elif i > 0:
                i = lps[i-1]
            else :
                j += 1
        return lps
    def kmp(self,text,pattern):
        lps = self.findLPS(pattern)
        i,j=0,0
        ans = list()
        while j < len(text):
            if text[j] == pattern[i]:
                i += 1
                j += 1
                if i == len(pattern):
                    ans.append(j-i)
            elif i > 0:
                i = lps[i-1]
            else:
                j += 1
        return ans                         

