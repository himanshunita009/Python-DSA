class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solve(self,postorder: list[int],postStart: int,postEnd: int,inorder: list[int],inStart: int,inEnd: int):
        if postStart > postEnd:
            return None
        temp =  inEnd
        while temp >= inStart and inorder[temp] != postorder[postEnd]:
            temp -1= 1
        rightLen = inEnd - temp
        right = self.solve(postorder,postEnd-rightLen,postEnd-1,inorder,temp+1,inEnd)
        left = self.solve(postorder,postStart,postEnd-rightLen-1,inorder,inStart,temp-1)
        return TreeNode(postorder[postEnd],left,right)

    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        return self.solve(postorder,0,len(postorder)-1,inorder,0,len(inorder)-1)