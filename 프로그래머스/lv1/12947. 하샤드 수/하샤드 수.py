def solution(x):
    hashard = 0
    for i in range(len(str(x))):
        hashard += int(str(x)[i])
    if x%hashard == 0: 
        return True
    else: 
        return False