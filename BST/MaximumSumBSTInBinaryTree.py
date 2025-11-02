# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def solve(self,root: TreeNode):
        if not root:
            return [True,0,float('inf'),float('-inf')]
        left = self.solve(root.left)
        right = self.solve(root.right)
        leftVal = root.left.val if root.left else float('-inf')
        rightVal = root.right.val if root.right else float('inf')
        if left[0] and right[0] and leftVal < root.val < rightVal and left[3] < root.val < right[2]:
            self.ans = max(self.ans,left[1]+right[1]+root.val)
            return [True,left[1]+right[1]+root.val,max(root.val,left[3]),min(root.val,right[2])]
        return [False,0]
    def maxSumBST(self, root: TreeNode) -> int:
        self.solve(root)
        return self.ans