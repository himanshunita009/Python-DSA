class Solution: 
    def getNextChar(self,ch: chr): 
        if ch == "z": return "a" 
        return chr(ord(ch)+1) 
    def findTheString(self, lcp: list[list[int]]) -> str: 
        n = len(lcp) 
        arr = ["a" for _ in range(n)] 
        for row in range(n): 
            for col in range(n): 
                eq = lcp[row][col] 
                if eq > min(n-row,n-col): 
                    return "" 
                i = row 
                j = col 
                while i < n and j < n: 
                    if eq > 0 : 
                        if arr[i] != arr[j]: 
                            if i < j:
                                arr[j] = arr[i]
                            else:
                                arr[i] = arr[j] 
                            eq -= 1 
                    else: 
                        if arr[i] == arr[j]: 
                            nxtChar = self.getNextChar(arr[i]) 
                            if i < j: 
                                arr[j] = nxtChar 
                            else: 
                                arr[i] = nxtChar 
                                
                    i += 1 
                    j += 1 
        return "".join(arr)