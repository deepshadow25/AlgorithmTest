def solution(n):
    for i in range(1,n+1):
        if i**2 == n:
            return (i+1)**2
        elif i**2 < n:
            i += 1
            continue
        else:
            return -1