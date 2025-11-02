class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = -1
    def solve(self,root,count,k):
        if self.ans == -1:
            if not root:
                return 0
            right = self.solve(root.right,count,k)
            if(right+ count +1 == k):
                self.ans = root.data
            left = self.solve(root.left,count+right+1,k)
            return left + right + 1
    def kthLargest(self,root, k):
        self.solve(root,0,k)
        return self.ans