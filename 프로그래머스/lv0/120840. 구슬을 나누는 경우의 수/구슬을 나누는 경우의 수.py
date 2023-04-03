def solution(balls, share):
    fac = lambda n:n*fac(n-1) if n>1 else 1
    return fac(balls)/(fac(share)*fac(balls-share))