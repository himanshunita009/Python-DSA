class Solution:
    def __init__(self):
        self.ans = float('inf')
    def solve(self,num1: int , num2: int,op: int):
        if num1 < 0:
            return
        if num1 == 0:
            self.ans = max(self.ans,op)
            return
        for i in range(0,61):
            temp  = num1 - 2**i - num2
            self.solve(temp,num2,op+1)
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        self.solve(num1,num2,0)
        return self.ans