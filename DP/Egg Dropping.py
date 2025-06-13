class Solution:
    def eggDrop(self, n, floor):
        if floor <= 1 or n == 1:
            return floor
        ans = float('inf')
        for k in range(1,floor+1):
            temp = max(self.eggDrop(n-1,k-1),self.eggDrop(n,floor-k))+1
            ans = min(ans,temp)
            
        return ans
obj = Solution()
print(obj.eggDrop(2,10))