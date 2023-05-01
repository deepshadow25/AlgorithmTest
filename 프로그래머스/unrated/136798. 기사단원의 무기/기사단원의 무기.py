def solution(number, limit, power):
    return sum([i if i <= limit else power for i in divisor(number)])

def divisor(number):
    divisor = []
    for j in range(1, number+1):
        cnt = 0
        for i in range(1, int(j**0.5) +1):
            if j == i**2:
                cnt += 1
            elif j%i == 0:
                cnt += 2
        divisor.append(cnt)
    return divisor