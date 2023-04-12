from itertools import combinations

def solution(nums):
    result = 0
    for comb in combinations(nums, 3):
        if prime(sum(comb)):
            result += 1
        else:
            continue
    return result
        
def prime(x):
    if x%2 !=0 and all([x%i!=0 for i in range(3, int(x**0.5)+1, 2)]):
        return 1
    else: return 0