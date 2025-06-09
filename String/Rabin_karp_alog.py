class Solution():
    def __init__(self):
        self.base = 256
        self.mod = 10**9+7
    def hash(self,currHash,char):    
        return (currHash * self.base + ord(char))%self.mod
    def high_pow(self,m):
        return pow(self.base,m-1,self.mod)
    def rabin_karp(self,text: str,pattern: str):
        j,i,hashSum = 0,0,0
        targetSum = 0
        for char in pattern:
            targetSum = self.hash(targetSum,char)
        while j < len(text):
            hashSum = self.hash(hashSum,text[j])
            if j-i+1 == len(pattern) :
                if hashSum == targetSum:
                    for k in range(i,j+1):
                        if text[k] != pattern[k-i]:
                            break
                    return i
                else:
                    hashSum =  (hashSum - ord(text[i])*self.high_pow(len(pattern)))%self.mod
                i += 1
            j += 1
        return -1
    