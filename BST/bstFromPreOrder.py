# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self,nums: list[int],start: int,end: int):
        if start > end:
            return None
        piVot = start+1
        while piVot <= end:
            if nums[piVot] > nums[start]:
                break
        left = self.solve(nums,start+1,piVot-1)
        right = self.solve(nums,piVot,end)
        return TreeNode(nums[start],left,right)

    def bstFromPreorder(self, nums: list[int]) -> TreeNode:
        return self.solve(nums,0,len(nums)-1)


obj = Solution()
obj.bstFromPreorder([8,5,1,7,10,12])