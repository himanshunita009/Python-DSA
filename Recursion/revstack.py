def put(stack: list,element):
    if len(stack) == 0:
        stack.append(element)
        return
    top = stack.pop()
    put(stack,element)
    stack.append(top)
    
def solve(stack : list):
    if len(stack) == 0:
        return
    top = stack.pop()
    solve(stack)
    put(stack,top)
lst = [1,2,3,4,5]
solve(lst)
print(lst)