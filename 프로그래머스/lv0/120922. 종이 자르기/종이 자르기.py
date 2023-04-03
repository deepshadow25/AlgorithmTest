def solution(M, N):
    if M==1 and M==N:
        return 0
    if M!=1 and M==N:
        return (M**2) -1
    else:
        return (M*N) -1