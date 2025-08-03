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
        mid = (start+end)//2
        left = self.solve(nums,start,mid-1)
        right = self.solve(nums,mid+1,end)
        return TreeNode(nums[mid],left,right)

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        return self.solve(nums,0,len(nums)-1)