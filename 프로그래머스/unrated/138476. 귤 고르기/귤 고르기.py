from collections import Counter

def solution(k, tangerine):
    cnt, answer = 0, 0
    for i,j in Counter(tangerine).most_common(k):
        cnt += j
        answer += 1
        if cnt >= k:            
            return answer