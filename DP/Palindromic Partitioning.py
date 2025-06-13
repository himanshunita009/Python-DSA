# class Solution:
#     def isPlainDrom(self,s: str):
#         for i in range(len(s)//2):
#             if s[i] != s[-(i+1)]:
#                 return False
#         return True
        
        
#     def palPartition(self, s):
#         if self.isPlainDrom(s):
#             return 0
#         minPartitioning = 10**4
#         for i in range(len(s)):
#             prefix = s[:i+1]
#             if self.isPlainDrom(prefix):
#                 minPartitioning = min(minPartitioning,self.palPartition(s[i+1:])+1)
#         return minPartitioning


class Solution:
    def __init__(self):
        self.dp = dict()
    def isPlainDrom(self,s: str):
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                return False
        return True
                
    def palPartition(self, s):
        if s in self.dp:
            return self.dp[s]
        if self.isPlainDrom(s):
            return 0       
        minPartitioning = 10**4
        for i in range(len(s)):
            prefix = s[:i+1]
            if self.isPlainDrom(prefix):
                minPartitioning = min(minPartitioning,self.palPartition(s[i+1:])+1)
        self.dp[s] = minPartitioning
        return self.dp[s]


