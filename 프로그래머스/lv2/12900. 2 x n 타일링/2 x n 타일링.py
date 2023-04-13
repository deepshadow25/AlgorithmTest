def solution(n):
    F = [1, 2]
    for i in range(2, n+1):
        F.append((F[-1]+F[-2])%1000000007)
    return F[n-1]%1000000007