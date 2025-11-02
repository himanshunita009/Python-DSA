class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findInOrder(self,root: TreeNode,inorder: list[int]):
        if root:
            self.findInOrder(root.left,inorder)
            inorder.append(root.val)
            self.findInOrder(root.right,inorder)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        inorder = []
        self.findInOrder(root,inorder)
        i =0 
        j = len(inorder)-1
        while i < j:
            if inorder[i] + inorder[j] > k:
                j -= 1
            elif inorder[i]+inorder[j] < k:
                i += 1
            else: 
                return True
        return False