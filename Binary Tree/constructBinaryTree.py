class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solve(self,preorder: list[int],preStart: int,preEnd: int,inorder: list[int],inStart: int,inEnd: int):
        tempInEnd =  inStart
        while tempInEnd <= inEnd and inorder[tempInEnd] != preorder[preStart]:
            tempInEnd += 1
        leftLen = tempInEnd - inStart
        left = self.solve(preorder,preStart+1,preStart+1+leftLen,inorder,inStart,tempInEnd-1)
        right = self.solve(preorder,preStart+1,preStart+1+leftLen,inorder,inStart,tempInEnd-1)


    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        root = preorder