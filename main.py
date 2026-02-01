class Solution:
    def solve(self,currIdx: int,prevIdx: int,k: int):
        if k == 0:
            return self.nums[currIdx]
        elif currIdx == len(self.nums):
            return float('inf')
        if (currIdx,prevIdx,k) in self.dp:
            return self.dp[(currIdx,prevIdx,k)]
        partition = self.nums[prevIdx+1] + self.solve(currIdx+1,currIdx,k-1)
        notPartition = float('inf')
        if k < len(self.nums)-1 - currIdx:
            notPartition = self.solve(currIdx+1,prevIdx,k)
        self.dp[(currIdx,prevIdx,k)] = min(partition,notPartition)
        return self.dp[(currIdx,prevIdx,k)]

    def minPartitionScore(self, nums: list[int]) -> int:
        self.nums = nums
        self.dp = dict()
        return self.solve(0,-1,2)
    
obj = Solution()
print(obj.minPartitionScore([10,3,1,1]))