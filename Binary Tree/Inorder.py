class Node :
    def __init__(self,x=0):
        self.left : Node = None
        self.right : Node = None
        self.val : int = x
def inorderTravetsal(root: Node):
    curr = root
    stack = []

    while curr is not None or stack:
        while curr :
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr.val)
        curr = curr.right