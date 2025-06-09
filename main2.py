import math
class Solution(object):
    def compute_lps(self,pattern):
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def kmp_search(self,text, pattern):
        n = len(text)
        m = len(pattern)
        lps = self.compute_lps(pattern)

        indices = []  # to store starting indexes where pattern is found
        i = 0
        j = 0

        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1

            if j == m:
                indices.append(i - j)  # found a match
                j = lps[j - 1]
            elif i < n and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return indices
        
    def convertHString(self,grid):
        ans = ""
        for gr in grid:
            for ch in gr:
                ans += ch
        return ans

    def convertVString(self,grid):
        ans = ""
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                ans += grid[i][j]
        return ans
    def countCells(self, grid, pattern):
        hstr = self.convertHString(grid)
        vstr = self.convertVString(grid)
        hstridx = self.kmp_search(hstr,pattern)
        vstridx = self.kmp_search(vstr,pattern)
        print(hstridx)
        print(vstridx)
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for k in range(len(hstridx)):
            for i in range(hstridx[k],hstridx[k]+len(pattern)):
                row = i//m
                col = i- (row*m)
                grid[row][col] = '.'
        for k in range(len(vstridx)):
            for i in range(vstridx[k],vstridx[k]+len(pattern)):
                col = i//n
                row = i- (col*n)
                if grid[row][col] == '.':
                    ans += 1
                    grid[row][col] = '.'
        return ans        

obj = Solution()
print(obj.countCells([["c","a","a","a"],["a","a","b","a"],["b","b","a","a"],["a","a","b","a"]],"aba"))
