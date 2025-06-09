def put(stack: list,element):
    if len(stack) == 0:
        stack.append(element)
        return
    top = stack[len(stack) - 1]
    if top > element:
        stack.pop()
        put(stack,element)
        stack.append(top)
    else:
        stack.append(element)
    
def solve(stack : list):
    if len(stack) == 0:
        return
    top = stack.pop()
    solve(stack)
    put(stack,top)
lst = [5,-2,9,-7,3]
solve(lst)
print(lst)