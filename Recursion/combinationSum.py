class Solution:
    def __init__(self):
        self.ans = list()
        self.target = 0
        self.nums = list()
    def solve(self,i,tsum,temp): 
        if tsum > self.target:
            return 
        if i == len(self.nums):
            if tsum == self.target:
                self.ans.append(temp)
            return
        self.solve(i+1,tsum,temp)
        t2 = temp.copy()
        t2.append(self.nums[i])
        self.solve(i,tsum+self.nums[i],t2)

    def combinationSum(self, candidates, target):
        self.target = target
        self.nums = candidates
        self.solve(0,0,[])
        return self.ans
    
obj = Solution()
print(obj.combinationSum([2,3,5],8))
