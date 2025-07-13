# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = None
    def solve(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if self.ans:
            return None
        if not root:
            return None
        left = self.solve(root.left,p,q)
        right = self.solve(root.right,p,q)
        if root.val in [p,q]:
            if left and left.val in [p,q] or right or right.val in [p,q]:
                self.ans = root
        if left and left.val in [p,q] and right or right.val in [p,q]:
                self.ans = root
        if root.val in [p,q]:
            return root
        if left and left.val in [p,q]:
            return left
        if right and right.val in [p,q]:
            return right
        return None
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.solve(root,p,q)
        return self.ans