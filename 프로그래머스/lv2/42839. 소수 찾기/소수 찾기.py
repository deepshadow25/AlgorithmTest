from itertools import permutations

def prime(number):
    num = int(number)
    for p in range(2, int(num**0.5)+1):
        if num % p == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    number = list(numbers)
    perms = []
    
    for i in range(1, len(number)+1):
        for perm in permutations(number, i):
            perms.append(''.join(perm))
    perms = list(set(perms))
    
    for num in perms:
        if num[0] != '0' and num != '1':
            if prime(num) == True:
                answer += 1
    return answer