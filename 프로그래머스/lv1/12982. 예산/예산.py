from collections import deque
def solution(d, budget):
    answer = 0
    d = deque(sorted(d))
    for i in d:
        budget -= i
        if budget < 0:
            break
        answer += 1
    return answer
        