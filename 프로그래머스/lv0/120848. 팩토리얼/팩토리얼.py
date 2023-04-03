fac = lambda n:n*fac(n-1) if n>1 else 1

def solution(n):
    i = 1
    while fac(i) <= n:
        i += 1
    else:
        return i-1