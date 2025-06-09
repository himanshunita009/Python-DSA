class Solution(object):
    
    def __init__(self):
        self.INT_MAX = 2**31-1
        self.INT_MIN = -(2**31)

    def solve(self,s,n,num):
        if n == len(s) or s[n] < '0' or s[n] > '9':
            return num
        
        if num > self.INT_MAX:   
            return self.INT_MAX
        return self.solve(s,n+1,num*10+int(s[n]))
        
    def myAtoi(self, s):
        s = s.strip()
        isNegative = s[0] == '-'
        if (s[0] == '-' or s[0] == '+'):
            s = s[1:]
        num = self.solve(s,0,0)
        if isNegative and num == self.:

        return -num if isNegative else num        
        