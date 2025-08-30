class Solution:
    def __init__(self):
        self.evenPrefix = [2*x  for x in range(1,500)]
        self.oddPrefix = [2*x-1  for x in range(1,500)]
        for idx in range(1,len(self.evenPrefix)):
            self.evenPrefix[idx] += self.evenPrefix[idx-1]
        
        for idx in range(1,len(self.oddPrefix)):
            self.oddPrefix[idx] += self.oddPrefix[idx-1]
    def findGcd(self,a,b):
        if b ==0:
            return a
        return self.findGcd(b,a%b)
        
    def gcdOfOddEvenSums(self, n: int) -> int:
        return self.findGcd(self.evenPrefix[n-1],self.oddPrefix[n-1])        


obj = Solution()
print(obj.gcdOfOddEvenSums(5))