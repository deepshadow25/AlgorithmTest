import math

def solution(n,a,b):
    a, b = min(a, b), max(a, b)
    answer = 1
    while 1:
        if a%2 == 1 and a+1==b:
            break
        a, b = math.ceil(a/2), math.ceil(b/2)
        answer+=1
    return answer