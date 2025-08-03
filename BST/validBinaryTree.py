# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = root.left.val if root.left else float("-inf") 
        right = root.right.val if root.right else float("inf")
        if left <= root.val <= right:
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        return False 