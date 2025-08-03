class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solve(self,preorder: list[int],preStart: int,preEnd: int,inorder: list[int],inStart: int,inEnd: int):
        if preStart > preEnd:
            return None
        tempInEnd =  inStart
        while tempInEnd <= inEnd and inorder[tempInEnd] != preorder[preStart]:
            tempInEnd += 1
        leftLen = tempInEnd - inStart
        left = self.solve(preorder,preStart+1,preStart+leftLen,inorder,inStart,tempInEnd-1)
        right = self.solve(preorder,preStart+leftLen+1,preEnd,inorder,tempInEnd+1,inEnd)
        return TreeNode(preorder[preStart],left,right)

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        return self.solve(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)