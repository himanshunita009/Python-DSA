class Solution:
    def __init__(self):
        self.n = 0
        self.delay  = 0
        self.forget  = 0
        self.mod = 10**9+7
        self.mp = dict()
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        self.n = n-1
        self.delay = delay-1
        self.forget = forget-1
        return self.solve(n-1,delay-1,forget-1)%self.mod
    
    def solve(self,n,d,f):
        if n == 0 :
            return 1
        if  f == 0:
            return 0
        if (n,d,f) in self.mp:
            return self.mp.get((n,d,f))
        if d > 0:
            self.mp[(n,d,f)] = self.solve(n-1,d-1,f-1)
        else:
            self.mp[(n,d,f)] =  (self.solve(n-1,d,f-1) + self.solve(n-1,self.delay,self.forget))%self.mod
        return self.mp.get((n,d,f))
            

obj = Solution()
print(obj.peopleAwareOfSecret(4,1,4))
        