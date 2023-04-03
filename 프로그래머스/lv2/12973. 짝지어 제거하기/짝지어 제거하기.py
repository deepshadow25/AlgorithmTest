def solution(s):
    if len(s)%2 == 1: 
        return 0
    if len(s)==2 and s[0] == s[1]:
        return 1
    
    stack = [s[0]]
    for c in s[1:]:
        if len(stack) > 0 and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
            
    if len(stack) != 0:
        return 0
    else:
        return 1