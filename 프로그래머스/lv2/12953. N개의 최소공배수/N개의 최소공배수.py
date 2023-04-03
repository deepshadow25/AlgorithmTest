import math
lcm=lambda x,y:int(x*y/ math.gcd(x,y))

def solution(arr):
    stack = []
    for x in arr:
        if not stack:
            stack.append(x)
        else:
            stack.append(lcm(stack.pop(), x))         
    return stack[-1]