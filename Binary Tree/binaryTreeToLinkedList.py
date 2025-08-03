# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is not None:
            if root.left is None and root.right is None:
                return root 
            left = self.flatten(root.left)
            temp = root.right
            if left:
                root.right = root.left
                left.right = temp
            root.left = None
            right = self.flatten(temp)
            return right if right is not None else left
        return None