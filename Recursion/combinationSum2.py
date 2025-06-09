class Solution:
    def __init__(self):
        self.ans = set()
        self.target = 0
        self.nums = list()
    def solve(self,i,tsum,temp: list): 
        if tsum > self.target:
            return 
        if i == len(self.nums):
            if tsum == self.target:
                self.ans.add(temp)
            return
        self.solve(i+1,tsum,temp)
        if tsum+self.nums[i] <= self.target:
            t2 = temp[:]
            t2.append(self.nums[i])
            self.solve(i+1,tsum+self.nums[i],t2)

    def combinationSum2(self, candidates: list, target):
        candidates.sort()
        self.target = target
        self.nums = candidates
        self.solve(0,0,[])
        return list(self.ans)


obj = Solution()
print(obj.combinationSum2([10,1,2,7,6,1,5],8))
