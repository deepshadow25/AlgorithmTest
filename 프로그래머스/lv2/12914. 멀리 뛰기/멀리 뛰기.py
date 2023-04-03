def 피보나치수열(n):
	F = [0, 1]
	for i in range(2, n+1):
		F.append(F[i-2]+F[i-1])
	return F[n]%1234567

def solution(n):
    return 피보나치수열(n+1)